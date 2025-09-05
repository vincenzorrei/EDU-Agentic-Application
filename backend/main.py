import asyncio
import json

from agent.agent import MovieChatAgent
from config import Config
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketState
from websockets.exceptions import ConnectionClosedError

app = FastAPI(title="Netflix AI Chat Backend")

# Configura CORS per permettere connessioni dal frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In produzione: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = Config()

# Inizializza agent globale
movie_agent = MovieChatAgent(config)


@app.websocket("/chat/{user_id}")
async def chat_endpoint(websocket: WebSocket, user_id: str):
    """
    WebSocket endpoint per chat real-time
    Gestisce conversazioni persistenti per user_id
    """
    await websocket.accept()

    # 🧪 TEST: Usa un ID fisso per testare se il problema è nell'UUID lungo
    actual_user_id = "vincenzo01"  # Temporaneo per test
    print(
        f"💬 Nuovo utente connesso: '{user_id}' -> usando '{actual_user_id}' per test"
    )

    # Flag per evitare chiusure multiple
    connection_closed = False

    try:
        while not connection_closed:
            try:
                # Ricevi messaggio utente con timeout
                user_message = await asyncio.wait_for(
                    websocket.receive_text(), timeout=300.0  # 5 minuti di timeout
                )

                print(f"📥 Messaggio ricevuto: '{user_message[:50]}...'")

                # Verifica che la connessione sia ancora valida
                if websocket.client_state != WebSocketState.CONNECTED:
                    print(f"⚠️ WebSocket non più connesso prima del processing")
                    break

                # Process message in a separate task to avoid blocking
                try:
                    # Esegui il processing in modo asincrono
                    loop = asyncio.get_event_loop()
                    response = await loop.run_in_executor(
                        None, movie_agent.process_message, user_message, actual_user_id
                    )

                    print(f"✅ Risposta generata, lunghezza: {len(response)}")

                    # Sanitizza la risposta per evitare problemi di encoding
                    if response:
                        # Rimuovi caratteri problematici
                        response = response.replace("\x00", "")  # Null bytes
                        response = "".join(
                            char
                            for char in response
                            if ord(char) < 127 or ord(char) > 31
                        )

                        # Se la risposta è troppo lunga, dividila in chunks
                        MAX_CHUNK_SIZE = 4096  # 4KB per chunk
                        if len(response) > MAX_CHUNK_SIZE:
                            print(
                                f"📦 Risposta lunga ({len(response)} bytes), invio in chunks..."
                            )

                            # Invia un messaggio speciale per indicare l'inizio di una risposta chunked
                            await websocket.send_text(
                                json.dumps(
                                    {
                                        "type": "chunk_start",
                                        "total_length": len(response),
                                    }
                                )
                            )

                            # Invia la risposta in chunks
                            for i in range(0, len(response), MAX_CHUNK_SIZE):
                                chunk = response[i : i + MAX_CHUNK_SIZE]
                                chunk_data = json.dumps(
                                    {
                                        "type": "chunk",
                                        "content": chunk,
                                        "index": i // MAX_CHUNK_SIZE,
                                    }
                                )

                                # Verifica connessione prima di ogni invio
                                if websocket.client_state == WebSocketState.CONNECTED:
                                    await websocket.send_text(chunk_data)
                                    # Piccola pausa tra i chunks per evitare overflow
                                    await asyncio.sleep(0.01)
                                else:
                                    print(f"⚠️ Connessione persa durante invio chunks")
                                    connection_closed = True
                                    break

                            if not connection_closed:
                                # Invia messaggio di fine chunks
                                await websocket.send_text(
                                    json.dumps({"type": "chunk_end"})
                                )
                        else:
                            # Risposta normale (non chunked)
                            if websocket.client_state == WebSocketState.CONNECTED:
                                # Invia come JSON per maggiore robustezza
                                await websocket.send_text(
                                    json.dumps({"type": "message", "content": response})
                                )
                                print(f"📤 Risposta inviata con successo")
                            else:
                                print(f"⚠️ WebSocket disconnesso prima dell'invio")
                                connection_closed = True

                except Exception as process_error:
                    print(f"❌ Errore durante processing: {process_error}")
                    import traceback

                    traceback.print_exc()

                    # Invia messaggio di errore se la connessione è ancora attiva
                    if websocket.client_state == WebSocketState.CONNECTED:
                        error_msg = json.dumps(
                            {
                                "type": "error",
                                "content": "Mi dispiace, ho riscontrato un problema. Riprova tra qualche istante.",
                            }
                        )
                        await websocket.send_text(error_msg)

            except asyncio.TimeoutError:
                print(f"⏱️ Timeout in attesa del messaggio per utente: {actual_user_id}")
                # Invia un ping per verificare se la connessione è ancora attiva
                if websocket.client_state == WebSocketState.CONNECTED:
                    try:
                        await websocket.send_text(json.dumps({"type": "ping"}))
                    except:
                        connection_closed = True
                        break

            except WebSocketDisconnect as e:
                print(f"🔌 Utente disconnesso: {actual_user_id} - Codice: {e.code}")
                connection_closed = True
                break

            except ConnectionClosedError as e:
                print(f"🔌 Connessione chiusa: {actual_user_id} - {e}")
                connection_closed = True
                break

            except Exception as e:
                print(f"❌ Errore inaspettato: {e}")
                import traceback

                traceback.print_exc()
                connection_closed = True
                break

    except Exception as e:
        print(f"❌ Errore nella chat per {actual_user_id}: {e}")

    finally:
        # Chiusura sicura
        try:
            if (
                not connection_closed
                and websocket.client_state == WebSocketState.CONNECTED
            ):
                await websocket.close(code=1000, reason="Chat session ended")
                print(f"✅ WebSocket chiuso correttamente per {actual_user_id}")
        except Exception as e:
            print(f"⚠️ Errore durante chiusura WebSocket: {e}")


@app.get("/health")
async def health_check():
    return {"status": "healthy", "agent": "ready"}


@app.get("/test-info")
async def test_info():
    """Endpoint per verificare configurazione"""
    return {
        "backend_status": "running",
        "websocket_endpoint": "/chat/{user_id}",
        "user_id_source": "dynamic_session_id",
        "description": "Ogni utente ha un SESSION_ID unico generato dal frontend",
        "chunking_enabled": True,
        "max_chunk_size": 4096,
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Avvio Netflix AI Chat Backend...")
    print("📡 WebSocket endpoint: ws://localhost:8000/chat/{user_id}")
    print("🔍 Health check: http://localhost:8000/health")
    print("🧪 Test info: http://localhost:8000/test-info")
    print("✅ Chunking abilitato per risposte lunghe")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="info")
