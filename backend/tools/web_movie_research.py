# backend/tools/web_movie_research.py
# -*- coding: utf-8 -*-
"""
WebMovieResearchTool (LCEL, RunnableParallel + unpack)

Pipeline:
1) Contextualization Prompt -> standalone query (history-aware)
2) RunnableParallel: Tavily + Reddit in parallelo
3) Unpack dei risultati paralleli in top-level (tavily, reddit)
4) Sintesi finale con LLM (italiano, senza spoiler)

Espone:
- .search(query, chat_history) -> str
- .as_structured_tool() -> StructuredTool (accetta query + chat_history)
"""

from __future__ import annotations

from operator import itemgetter
from typing import Any, Dict, List, Optional

from langchain_community.tools.reddit_search.tool import RedditSearchRun

# Community tools
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.reddit_search import RedditSearchAPIWrapper
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.tools import StructuredTool


# =============================================================================
# Config
# =============================================================================
class WebSearchConfig(BaseModel):
    # Tavily
    tavily_api_key: str = Field(..., description="API key Tavily.")
    tavily_max_results: int = Field(
        6, description="Numero massimo risultati da Tavily."
    )
    tavily_search_depth: Optional[str] = Field(
        default=None,
        description="Profondità ricerca Tavily ('basic' | 'advanced'), opzionale.",
    )
    include_images: bool = False  # non usato nella sintesi, ma disponibile

    # Reddit
    reddit_client_id: str
    reddit_client_secret: str
    reddit_user_agent: str
    reddit_max_results: int = Field(
        8, description="Numero massimo risultati da Reddit."
    )
    reddit_subreddit: str = Field(
        "movies", description="Subreddit principale da interrogare."
    )


# =============================================================================
# Implementazione LCEL con RunnableParallel + unpack
# =============================================================================
class WebMovieResearchTool:
    """
    Ricerca web su film con Tavily + Reddit in parallelo.
    - Rewriter history-aware della query
    - Parallelizzazione esplicita con RunnableParallel
    - Sintesi LLM in italiano, senza spoiler
    """

    def __init__(self, config: WebSearchConfig, llm: BaseChatModel):
        self.config = config
        self.llm = llm

        # ------ (1) Contextualization Prompt -> standalone query ----------------
        contextualization_prompt_text = (
            "Given a chat history and the latest user question which might reference context "
            "in the chat history, formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question; return only the rewritten query."
        )

        self.contextualization_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualization_prompt_text),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # Chain: {input, chat_history} -> standalone_query (str)
        self.standalone_query_chain = (
            self.contextualization_prompt | self.llm | StrOutputParser()
        )

        # ------ (2) Tools: Tavily + Reddit -------------------------------------
        # Tavily
        self.tavily_tool = TavilySearchResults(
            tavily_api_key=self.config.tavily_api_key,
            max_results=self.config.tavily_max_results,
            include_answer=False,
            include_raw_content=False,
            include_images=self.config.include_images,
        )

        # Reddit
        reddit_wrapper = RedditSearchAPIWrapper(
            reddit_client_id=self.config.reddit_client_id,
            reddit_client_secret=self.config.reddit_client_secret,
            reddit_user_agent=self.config.reddit_user_agent,
        )
        self.reddit_tool = RedditSearchRun(api_wrapper=reddit_wrapper)

        # Runnables che lanciano i tool a partire da una standalone_query (str)
        def _run_tavily(q: str) -> Dict[str, Any]:
            tv_query = f"{q} movie reviews critics analysis"
            try:
                payload = {"query": tv_query}
                if self.config.tavily_search_depth:
                    payload["search_depth"] = self.config.tavily_search_depth
                res = self.tavily_tool.invoke(payload)
                return {"source": "tavily", "query": tv_query, "results": res}
            except Exception as e:
                return {
                    "source": "tavily",
                    "query": tv_query,
                    "results": [],
                    "error": str(e),
                }

        def _run_reddit(q: str) -> Dict[str, Any]:
            rd_query = f"{q} movie discussion"
            try:
                res = self.reddit_tool.invoke(
                    {
                        "query": rd_query,
                        "sort": "relevance",
                        "time_filter": "year",
                        "subreddit": self.config.reddit_subreddit,
                        "limit": str(self.config.reddit_max_results),
                    }
                )
                return {"source": "reddit", "query": rd_query, "results": res}
            except Exception as e:
                return {
                    "source": "reddit",
                    "query": rd_query,
                    "results": "",
                    "error": str(e),
                }

        self.tavily_runnable = RunnableLambda(_run_tavily)
        self.reddit_runnable = RunnableLambda(_run_reddit)

        # Parallel runner esplicito
        self.parallel = RunnableParallel(
            tavily=itemgetter("standalone_query") | self.tavily_runnable,
            reddit=itemgetter("standalone_query") | self.reddit_runnable,
        )

        # ------ (3) Prompt di sintesi ---------------------------------------------------
        self.synthesis_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Sei un ricercatore cinematografico che analizza fonti web e community.\n"
                    "REGOLE:\n"
                    "- Riassumi in italiano, in modo conciso e strutturato.\n"
                    "- NON fare spoiler (evita colpi di scena/finali).\n"
                    "- Se emergono opinioni contrastanti, evidenziale brevemente.\n"
                    "- Cita la provenienza delle informazioni in modo descrittivo (es. 'critic reviews', 'Reddit users'), "
                    "senza URL a meno che non siano essenziali.\n"
                    "- Se i risultati sono scarsi o rumorosi, dillo esplicitamente e suggerisci ricerche aggiuntive.\n",
                ),
                MessagesPlaceholder("chat_history"),
                (
                    "human",
                    "Richiesta originale: {input}\n\n"
                    "Standalone query: {standalone_query}\n\n"
                    "Risultati Tavily (riassumi i punti chiave):\n{tavily}\n\n"
                    "Risultati Reddit (topic ricorrenti, consenso/dissenso):\n{reddit}\n",
                ),
            ]
        )

        # ------ (4) Core chain: input -> standalone_query -> parallel -> unpack -> synth
        self.core_chain = (
            # Normalizza l'input in dict
            RunnableLambda(lambda x: x if isinstance(x, dict) else {"input": x})
            # Porta con sé la history (se manca, lista vuota)
            | RunnablePassthrough.assign(
                chat_history=lambda x: x.get("chat_history", [])
            )
            # Calcola standalone_query su {input, chat_history}
            | RunnablePassthrough.assign(standalone_query=self.standalone_query_chain)
            # Esegui Tavily + Reddit in parallelo -> campo "web" con {"tavily": ..., "reddit": ...}
            | RunnablePassthrough.assign(web=self.parallel)
            # Unpack in top-level: {tavily, reddit}
            | RunnableLambda(
                lambda x: {
                    **x,
                    "tavily": x["web"]["tavily"],
                    "reddit": x["web"]["reddit"],
                }
            )
            # Sintesi finale
            | self.synthesis_prompt
            | self.llm
            | StrOutputParser()
        )

    # -----------------------------------------------------------------------------
    # API
    # -----------------------------------------------------------------------------
    def search(self, query: str, chat_history: Optional[List[Any]] = None) -> str:
        """
        Esegue la pipeline:
        - Rewriter history-aware -> Standalone query
        - Tavily + Reddit in parallelo (RunnableParallel)
        - Unpack dei risultati
        - Sintesi finale (italiano, senza spoiler)
        """
        try:
            return self.core_chain.invoke(
                {"input": query, "chat_history": chat_history or []}
            )
        except Exception as e:
            return f"❌ Errore nella ricerca web: {e}"

    # -----------------------------------------------------------------------------
    # StructuredTool factory
    # -----------------------------------------------------------------------------
    class _Args(BaseModel):
        query: str = Field(..., description="Query utente per la ricerca web su film.")
        chat_history: Optional[List[Any]] = Field(
            default=None,
            description="Cronologia conversazionale per contestualizzare la query.",
        )

    def as_structured_tool(self) -> StructuredTool:
        """
        Restituisce uno StructuredTool 'web_movie_research' da registrare nell’orchestratore.
        Accetta 'query' e 'chat_history' e richiama .search() senza alterare la pipeline.
        """

        def _run(query: str, chat_history: Optional[List[Any]] = None) -> str:
            return self.search(query=query, chat_history=chat_history)

        return StructuredTool.from_function(
            name="web_movie_research",
            description=(
                "Ricerca web (Tavily + Reddit) su film: critica, recensioni e discussioni della community. "
                "Usa una standalone query history-aware e restituisce una sintesi in italiano senza spoiler."
                "Puoi usare per dare informazioni su un film o attori non presenti in Netflix ()."
            ),
            args_schema=self._Args,
            func=_run,
        )
