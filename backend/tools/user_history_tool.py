from langchain.chains import create_history_aware_retriever
from langchain_core.tools import Tool


class UserHistoryTool:
    """
    Tool per accesso alla conversation history degli utenti
    Lavora su mock data per demo purposes
    """

    def __init__(self, users_vectorstore, llm, config):
        self.vectorstore = users_vectorstore
        self.llm = llm
        self.config = config

        # Crea retriever per user history
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 3}  # Max 3 conversazioni passate
        )

    def get_user_history(self, user_id: str, current_query: str = "") -> str:
        """
        Recupera storia conversazioni per un utente specifico
        Usa filtro esatto sui metadata per garantire risultati corretti

        Args:
            user_id: ID utente
            current_query: Query corrente per context

        Returns:
            Storico conversazioni formattato
        """
        try:
            # FILTRO ESATTO per user_id nei metadata
            filter_dict = {"user_id": user_id}

            # Query semantica per il contenuto (se fornito)
            query = current_query if current_query else "conversazioni utente"

            # Ricerca con filtro esatto sui metadata
            docs = self.vectorstore.similarity_search(
                query=query,
                k=3,  # Max 3 conversazioni
                filter=filter_dict,  # FILTRO ESATTO per user_id
            )

            if not docs:
                return f"🆕 Primo incontro con l'utente {user_id}"

            # Formatta storico conversazioni
            history_text = f"📋 **STORICO CONVERSAZIONI - Utente {user_id}:**\n\n"

            for i, doc in enumerate(docs, 1):
                meta = doc.metadata

                # Verifica doppia di sicurezza (dovrebbe essere superflua con il filtro)
                if meta.get("user_id") != user_id:
                    continue

                history_text += (
                    f"{i}. **{meta['user_name']}** ({meta['conversation_date']})\n"
                )
                history_text += f"   Preferenze: {', '.join(meta['preferences'][:3])}\n"
                history_text += (
                    f"   Film discussi: {', '.join(meta['discussed_films'][:2])}\n"
                )

                # Estratto conversazione
                summary = (
                    doc.page_content.split("Riassunto conversazione:")[1][:200]
                    if "Riassunto conversazione:" in doc.page_content
                    else ""
                )
                if summary:
                    history_text += f"   Riassunto: {summary.strip()}...\n"

                history_text += "\n"

            return history_text

        except Exception as e:
            return f"❌ Errore recupero storico: {str(e)}"

    def create_tool(self) -> Tool:
        """Crea langchain Tool object"""

        def user_history_lookup(user_query: str) -> str:
            """
            Recupera storico conversazioni dell'utente per personalizzare raccomandazioni.
            Formato query: "user_id:USER_ID [contesto_opzionale]"
            Esempio: "user_id:user123 film horror preferiti"
            """
            # Parse user_id dalla query
            if "user_id:" in user_query:
                parts = user_query.split(" ", 1)
                user_id = parts[0].replace("user_id:", "")
                context = parts[1] if len(parts) > 1 else ""
            else:
                return "❌ Specifica user_id nel formato: user_id:USER_ID"

            return self.get_user_history(user_id, context)

        return Tool(
            name="user_conversation_history",
            func=user_history_lookup,
            description="Retrieve user's old conversation summaries for personalized recommendations."
            "Use format: 'user_id:USER_ID [optional_context]'. Example: 'user_id:user123 horror preferences'",
        )
