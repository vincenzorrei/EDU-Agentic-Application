import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    """Configurazione centralizzata per il backend"""

    # API Keys
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY")
    reddit_client_id: str = os.getenv("REDDIT_CLIENT")
    reddit_client_secret: str = os.getenv("REDDIT_SECRET")
    reddit_user_agent: str = os.getenv("REDDIT_USER_AGENT", "NetflixAI/1.0")

    # Vector Store Paths (Chroma)
    films_vectorstore_path: str = "./data/chroma_films"
    users_vectorstore_path: str = "./data/chroma_users"

    # Model Settings
    llm_model: str = "gpt-4o"
    llm_temperature: float = 0.1
    max_tokens: int = 1000

    # Search Settings
    tavily_max_results: int = 5
    reddit_max_results: int = 10
    films_search_k: int = 5
    include_images: bool = False

    # Memory Settings
    conversation_memory_k: int = 10

    def validate(self):
        """Valida che tutte le API keys necessarie siano presenti"""
        required_keys = [
            self.openai_api_key,
            self.tavily_api_key,
            self.reddit_client_id,
            self.reddit_client_secret,
        ]

        if not all(required_keys):
            raise ValueError("API keys mancanti! Controlla le variabili d'ambiente.")
