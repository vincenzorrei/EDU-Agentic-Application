# backend/tools/movie_database_search.py
# -*- coding: utf-8 -*-
"""
MovieDatabaseSearchTool (LCEL, fedele alla pipeline originale)

Pipeline:
1) Contextualization Prompt (history-aware query rewriting)
2) create_history_aware_retriever(llm, base_retriever, prompt)
3) QA system prompt (stuff) con MessagesPlaceholder('chat_history')
4) create_stuff_documents_chain(llm, qa_prompt)
5) create_retrieval_chain(retriever, question_answer_chain)

Espone:
- .search(query, chat_history) -> str
- .as_structured_tool() -> StructuredTool (accetta query + chat_history)
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool


# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
class MovieDBConfig(BaseModel):
    """Parametri per il retriever."""

    films_search_k: int = Field(5, description="Numero di documenti da recuperare (k).")
    default_metadata_filter: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Filtro metadati di default per il vector store (es. provider='netflix').",
    )


# -----------------------------------------------------------------------------
# Implementazione LCEL fedele
# -----------------------------------------------------------------------------
class MovieDatabaseSearchTool:
    """
    Tool RAG per ricerca film su vector store con history-aware retrieval.
    Accetta un vectorstore compatibile LangChain e un LLM chat.
    """

    def __init__(
        self,
        films_vectorstore,
        llm: BaseChatModel,
        config: Optional[MovieDBConfig] = None,
    ):
        self.vectorstore = films_vectorstore
        self.llm = llm
        self.config = config or MovieDBConfig()

        # ------ (1) Contextualization Prompt -----------------------------------
        contextualization_prompt_text = (
            "Given a chat history and the latest user question which might reference context "
            "in the chat history, formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question; return only the rewritten query."
        )

        self.contextualize_query_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualization_prompt_text),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # ------ (2) Base retriever + history-aware retriever -------------------
        search_kwargs = {"k": self.config.films_search_k}
        if self.config.default_metadata_filter:
            # Alcuni vector store usano "filter", altri "where"; qui seguiamo lo standard LangChain "filter".
            search_kwargs["filter"] = self.config.default_metadata_filter

        base_retriever = self.vectorstore.as_retriever(search_kwargs=search_kwargs)

        self.retriever = create_history_aware_retriever(
            llm=self.llm,
            retriever=base_retriever,
            prompt=self.contextualize_query_prompt,
        )

        # ------ (3) QA system prompt (stuff) -----------------------------------
        qa_system_prompt = (
            "You are the official Netflix movie recommendation assistant. "
            "Use ONLY the retrieved movie information to answer the user's question about films.\n\n"
            "RULES:\n"
            "- Always mention availability (included/rental/unavailable) when present\n"
            "- Include Netflix URLs for available movies\n"
            "- Focus on mood, atmosphere and emotional impact\n"
            "- Never spoil major plot twists or endings\n"
            "- If a film is not in the database, it is not available on Netflix.\n"
            "- Keep responses engaging but concise\n"
            "- Reply in Italian\n\n"
            "RETRIEVED CONTEXT:\n{context}"
        )

        self.qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # ------ (4) Stuff QA chain ---------------------------------------------
        self.question_answer_chain = create_stuff_documents_chain(
            self.llm, self.qa_prompt
        )

        # ------ (5) Retrieval chain end-to-end ---------------------------------
        # Input: {"input": <str>, "chat_history": <list of messages>}
        self.rag_chain = create_retrieval_chain(
            self.retriever, self.question_answer_chain
        )

    # -----------------------------------------------------------------------------
    # API fedele e trasparente
    # -----------------------------------------------------------------------------
    def search(self, query: str, chat_history: Optional[List[Any]] = None) -> str:
        """
        Esegue la RAG chain con history awareness e restituisce la risposta testuale.

        Args:
            query: la domanda dell'utente.
            chat_history: lista di messaggi compatibili con MessagesPlaceholder (può essere []).

        Returns:
            La stringa in result["answer"] prodotta dalla retrieval chain.
        """
        try:
            result = self.rag_chain.invoke(
                {"input": query, "chat_history": chat_history or []}
            )
            # create_retrieval_chain ritorna un dict con chiave "answer" (e spesso anche "context")
            return result.get("answer", "")
        except Exception as e:
            return f"❌ Errore ricerca database: {e}"

    # -----------------------------------------------------------------------------
    # StructuredTool factory
    # -----------------------------------------------------------------------------
    class _Args(BaseModel):
        query: str = Field(
            ..., description="Query utente per la ricerca nel database film."
        )
        chat_history: Optional[List[Any]] = Field(
            default=None,
            description="Cronologia conversazionale per contestualizzare la query (può essere []).",
        )

    def as_structured_tool(self) -> StructuredTool:
        """
        Restituisce uno StructuredTool 'movie_database_search' da registrare nell'orchestratore.
        Accetta 'query' e 'chat_history' e richiama .search() senza alterare la pipeline.
        """

        def _run(query: str, chat_history: Optional[List[Any]] = None) -> str:
            return self.search(query=query, chat_history=chat_history)

        return StructuredTool.from_function(
            name="movie_database_search",
            description=(
                "Search Netflix movie database using plot descriptions, mood, genres, directors, and actors. "
                "Use to look if a movie is in the Netflix database."
                "case 1) If information about a film is not present in the database, it's NOT available on Netflix."
                "case 2) If the movie_search_tool gives any info about a film, it means the film IS AVAILABLE ON NETFLIX."
                "Supports semantic search and metadata filtering (USE ACCORDING TO THE REQUEST)."
                "Returns availability info and Netflix URLs when present in metadata."
                "Answers in Italian."
            ),
            args_schema=self._Args,
            func=_run,
        )
