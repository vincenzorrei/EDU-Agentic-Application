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

    try:
        while True:
            # Ricevi messaggio utente
            user_message = await websocket.receive_text()

            # Invece di ThreadPoolExecutor, esegui direttamente:
            print(f" Processing message directly (no ThreadPoolExecutor)")
            response = movie_agent.process_message(user_message, actual_user_id)
            print(f" Direct processing completed, response: '{response}'")

            # Verifica che la connessione sia ancora aperta prima di inviare
            if websocket.client_state == WebSocketState.CONNECTED:
                print(f"🔍 WebSocket still connected, sending response")
                try:
                    await websocket.send_text(response)
                    print(f" WebSocket response sent successfully")
                except Exception as send_error:
                    print(f"❌ Error sending response: {send_error}")
                    break
            else:
                print(
                    f"⚠️ Connessione chiusa durante processing per utente: {actual_user_id}"
                )
                break

    except WebSocketDisconnect as e:
        print(f"🔌 Utente disconnesso: {actual_user_id} - Codice: {e.code}")
    except ConnectionClosedError:
        print(f"🔌 Connessione chiusa prematuramente per utente: {actual_user_id}")
    except Exception as e:
        print(f"❌ Errore nella chat per {actual_user_id}: {e}")
    finally:
        # Chiusura sicura - controlla stato prima di chiudere
        try:
            if websocket.client_state == WebSocketState.CONNECTED:
                await websocket.close()
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
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Avvio Netflix AI Chat Backend...")
    print("📡 WebSocket endpoint: ws://localhost:8000/chat/{user_id}")
    print("🔍 Health check: http://localhost:8000/health")
    print("🧪 Test info: http://localhost:8000/test-info")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
