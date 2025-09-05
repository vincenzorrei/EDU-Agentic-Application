import os
from typing import Any, Dict, List

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from .films_data import get_enhanced_films_data
from .users_mock_data import get_mock_conversations


class DualVectorDatabase:
    """Gestisce 2 vector stores separati: films e users"""

    def __init__(self, config):
        self.config = config
        self.embeddings = OpenAIEmbeddings(api_key=config.openai_api_key)

        # Vector Stores
        self.films_store = None
        self.users_store = None

    def _convert_metadata_for_chroma(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converte metadati per compatibilità Chroma:
        - Liste -> stringhe separate da virgola
        - None -> "null" o skip
        - Mantiene str, int, float, bool
        """
        converted = {}
        for key, value in metadata.items():
            if value is None:
                # Skip valori None (Chroma non li accetta)
                continue
            elif isinstance(value, list):
                # Converti liste in stringhe
                converted[key] = ", ".join(str(item) for item in value)
            elif isinstance(value, dict):
                # Skip enhanced_description nei metadati Chroma (è già nel content)
                if key == "enhanced_description":
                    continue
                else:
                    converted[key] = str(value)
            elif isinstance(value, (str, int, float, bool)):
                # Tipi supportati direttamente
                converted[key] = value
            else:
                # Altri tipi -> stringa
                converted[key] = str(value)

        return converted

    def create_films_collection(self) -> Chroma:
        """
        Crea collection films con descrizioni molto ricche
        Focus su mood, atmosfere e trama dettagliata per semantic search
        """
        films_data = get_enhanced_films_data()
        documents = []

        for film in films_data:
            # Content MOLTO ricco per embedding
            content = self._create_rich_film_content(film)

            # Converti metadati per Chroma (liste -> stringhe)
            chroma_metadata = self._convert_metadata_for_chroma(film)

            doc = Document(page_content=content, metadata=chroma_metadata)
            documents.append(doc)

        # Crea vector store Chroma con persistenza automatica
        os.makedirs(self.config.films_vectorstore_path, exist_ok=True)
        films_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.config.films_vectorstore_path,
            collection_name="films",
        )

        print(f"✅ Films collection creata: {len(documents)} film")
        return films_store

    def create_users_collection(self) -> Chroma:
        """
        Crea collection users con mock conversation history
        """
        conversations = get_mock_conversations()
        documents = []

        for conv in conversations:
            content = f"""
            Conversazione con {conv['user_name']} del {conv['date']}
            
            Preferenze espresse: {', '.join(conv['preferences'])}
            Film discussi: {', '.join(conv['discussed_films'])}
            
            Riassunto conversazione:
            {conv['conversation_summary']}
            
            Mood preferiti: {', '.join(conv['preferred_moods'])}
            Generi apprezzati: {', '.join(conv['liked_genres'])}
            """

            # Converti metadati per Chroma
            chroma_metadata = self._convert_metadata_for_chroma(
                {
                    "user_id": conv["user_id"],
                    "user_name": conv["user_name"],
                    "conversation_date": conv["date"],
                    "preferences": conv["preferences"],  # Lista -> stringa
                    "discussed_films": conv["discussed_films"],  # Lista -> stringa
                }
            )

            doc = Document(
                page_content=content,
                metadata=chroma_metadata,
            )
            documents.append(doc)

        # Crea vector store Chroma con persistenza automatica
        os.makedirs(self.config.users_vectorstore_path, exist_ok=True)
        users_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.config.users_vectorstore_path,
            collection_name="users",
        )

        print(f"✅ Users collection creata: {len(documents)} conversazioni")
        return users_store

    def _create_rich_film_content(self, film: Dict[str, Any]) -> str:
        """
        Crea contenuto MOLTO RICCO per semantic search
        Focus su mood, emozioni, atmosfere, trama dettagliata
        """
        return f"""
        {film['title']} ({film['release_year']})
        
        GENERI E ATMOSFERA:
        {film['enhanced_description']['mood_description']}
        
        TRAMA COMPLETA:
        {film['enhanced_description']['detailed_plot']}
        
        STILE E REGIA:
        Diretto da {film['director']}. {film['enhanced_description']['directorial_style']}
        
        EMOZIONI E TEMI:
        {film['enhanced_description']['emotional_impact']}
        
        ESPERIENZA VISIVA:
        {film['enhanced_description']['visual_style']}
        
        CAST: {', '.join(film['cast'])}
        GENERI: {', '.join(film['genres'])}
        RATING: {film['imdb_rating']}/10 - {film['content_rating']}
        """

    def load_collections(self) -> tuple[Chroma, Chroma]:
        """Carica entrambe le collections da disco"""
        try:
            # Prova a caricare collections Chroma esistenti
            films_store = Chroma(
                persist_directory=self.config.films_vectorstore_path,
                embedding_function=self.embeddings,
                collection_name="films",
            )
            users_store = Chroma(
                persist_directory=self.config.users_vectorstore_path,
                embedding_function=self.embeddings,
                collection_name="users",
            )

            # Verifica che le collections abbiano dati
            films_count = films_store._collection.count()
            users_count = users_store._collection.count()

            if films_count == 0 or users_count == 0:
                print(
                    f"⚠️ Collections vuote (films: {films_count}, users: {users_count})"
                )
                raise ValueError("Collections vuote, ricreazione necessaria")

            print(f"✅ Vector stores Chroma caricati da disco")
            print(f"📊 Films: {films_count} documenti, Users: {users_count} documenti")
            return films_store, users_store

        except Exception as e:
            print(f"❌ Errore caricamento Chroma: {e}")
            print("🔄 Ricreo le collections...")

            films_store = self.create_films_collection()
            users_store = self.create_users_collection()

            return films_store, users_store
