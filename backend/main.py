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

    try:
        while True:
            # Ricevi messaggio utente
            user_message = await websocket.receive_text()

            # Processa messaggio con l'agent
            response = movie_agent.process_message(user_message, user_id)

            # Verifica che la connessione sia ancora aperta prima di inviare
            if websocket.client_state == WebSocketState.CONNECTED:
                try:
                    await websocket.send_text(response)
                except Exception as send_error:
                    print(f"Error sending response: {send_error}")
                    break
            else:
                break

    except WebSocketDisconnect as e:
        print(f"User disconnected: {user_id} - Code: {e.code}")
    except ConnectionClosedError:
        print(f"Connection closed prematurely for user: {user_id}")
    except Exception as e:
        print(f"Error in chat for {user_id}: {e}")
    finally:
        # Chiusura sicura - controlla stato prima di chiudere
        try:
            if websocket.client_state == WebSocketState.CONNECTED:
                await websocket.close()
        except Exception as e:
            print(f"Error during WebSocket closure: {e}")


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

    print("Starting Netflix AI Chat Backend...")
    print("WebSocket endpoint: ws://localhost:8000/chat/{user_id}")
    print("Health check: http://localhost:8000/health")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
