from typing import Dict

from database.vector_database import DualVectorDatabase
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from tools.movie_database_search import MovieDatabaseSearchTool
from tools.user_history_tool import UserHistoryTool
from tools.web_movie_research import WebMovieResearchTool


class MovieChatAgent:
    """
    Agent principale per conversazioni sui film Netflix
    Coordina 3 tools: movie_database_search, web_movie_research, user_conversation_history
    """

    def __init__(self, config):
        self.config = config

        # Inizializza LLM
        self.llm = ChatOpenAI(
            api_key=config.openai_api_key,
            model=config.llm_model,
            temperature=config.llm_temperature,
            max_tokens=config.max_tokens,
        )

        # Carica vector stores
        self.db_manager = DualVectorDatabase(config)
        self.films_store, self.users_store = self.db_manager.load_collections()

        # Crea tools
        self.tools = self._create_tools()

        # Crea agent executor
        self.agent_executor = self._create_agent_executor()

        # Session store per memory
        self._session_store: Dict[str, ChatMessageHistory] = {}

        # Agent con history
        self.agent_with_history = self._create_agent_with_history()

    def _create_tools(self):
        """Crea i 3 tools principali"""

        # Tool 1: Database search - usa as_structured_tool() per supportare chat_history
        from tools.movie_database_search import MovieDBConfig

        db_config = MovieDBConfig(
            films_search_k=self.config.films_search_k
            # default_metadata_filter non serve (è Optional)
        )

        db_search_tool = MovieDatabaseSearchTool(
            self.films_store, self.llm, db_config
        ).as_structured_tool()

        # Tool 2: Web research - crea config specifico
        from tools.web_movie_research import WebSearchConfig

        web_config = WebSearchConfig(
            tavily_api_key=self.config.tavily_api_key,
            tavily_max_results=self.config.tavily_max_results,
            reddit_client_id=self.config.reddit_client_id,
            reddit_client_secret=self.config.reddit_client_secret,
            reddit_user_agent=self.config.reddit_user_agent,
            reddit_max_results=self.config.reddit_max_results,
            include_images=self.config.include_images,
            reddit_subreddit="movies",  # Default value
        )

        web_research_tool = WebMovieResearchTool(
            web_config, self.llm
        ).as_structured_tool()

        # Tool 3: User history - questo va bene così
        user_history_tool = UserHistoryTool(
            self.users_store, self.llm, self.config
        ).create_tool()

        return [db_search_tool, web_research_tool, user_history_tool]

    def _create_agent_executor(self):
        """Crea REACT agent executor con prompt migliorato e parser robusto"""

        # Prompt più rigoroso con esempi espliciti
        system_prompt = """You are the official Netflix movie assistant that helps users find films.
        You have all the information about Netflix films availability from the database.
        Never search for Netflix film outside the database. If a film is not in the database, it is not available on Netflix.
        If the movie_search_tool gives some info about a film, it means the film is in the database.
        Never use emojis.

Available tools:
{tools}

Tool Names: {tool_names}

CRITICAL: You MUST follow the ReAct format EXACTLY. Each step must be on a new line.

FORMAT RULES:
1. Always start with "Thought:" on its own line
2. If using a tool, next line must be "Action:" followed by the exact tool name
3. Next line must be "Action Input:" followed by the input in quotes
4. Wait for "Observation:" (provided by system)
5. Continue with new "Thought:" or provide "Final Answer:"

EXAMPLE FORMAT:
Thought: I need to search for tension movies in the database
Action: movie_database_search
Action Input: "tension thriller movies"
Observation: [tool will provide output here]
Thought: Based on the results, I can now provide recommendations
Final Answer: Ecco alcuni film di tensione che potrebbero interessarti...

INSTRUCTIONS:
- Extract user_id from [USER_ID: xxx] if present
- Check user_conversation_history when needed
- Always respond in Italian in the Final Answer
- Include Netflix links when available
- Avoid spoilers
- Available films are presented using movie_database_search. Use ONLY this tool to get the availability information.

Question: {input}
Chat History: {chat_history}

{agent_scratchpad}"""

        prompt = PromptTemplate(
            template=system_prompt,
            input_variables=[
                "input",
                "chat_history",
                "agent_scratchpad",
                "tools",
                "tool_names",
            ],
        )

        # Crea REACT agent
        agent = create_react_agent(llm=self.llm, tools=self.tools, prompt=prompt)

        # Crea agent executor con parsing error handling migliorato
        agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=self._handle_parsing_error,  # Funzione custom
            max_iterations=5,
            return_intermediate_steps=False,
            # early_stopping_method="generate",  # Forza generazione di Final Answer
        )

        return agent_executor

    def _handle_parsing_error(self, error) -> str:
        """
        Gestisce gli errori di parsing in modo più intelligente
        """
        error_str = str(error)

        # Se l'output non segue il formato ReAct
        if "Could not parse" in error_str or "Invalid Format" in error_str:
            # Estrai eventuale contenuto utile dall'errore
            if "Ecco alcuni film" in error_str or "film che potrebbero" in error_str:
                # L'agent ha generato una risposta ma non nel formato corretto
                return """Thought: I need to properly format my response
Final Answer: Mi scuso per l'errore tecnico. Riprovo a cercare film di tensione per te. Potresti specificare meglio che tipo di tensione cerchi? (thriller psicologico, action, horror, suspense?)"""

            return """Thought: I encountered a formatting error and need to restart
Action: movie_database_search
Action Input: "film tensione thriller suspense"
"""

        # Per altri errori
        return f"""Thought: An error occurred: {error_str}. I should try a different approach.
Final Answer: Mi dispiace, ho riscontrato un problema tecnico. Potresti riformulare la tua richiesta?"""

    def _get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        """Recupera o crea chat history per session_id (user_id)"""
        if session_id not in self._session_store:
            self._session_store[session_id] = ChatMessageHistory()
        return self._session_store[session_id]

    def _create_agent_with_history(self):
        """Crea agent con RunnableWithMessageHistory"""
        return RunnableWithMessageHistory(
            self.agent_executor,
            self._get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="output",
        )

    def process_message(self, user_message: str, user_id: str) -> str:
        """
        Processa messaggio utente con AgentExecutor + History

        Args:
            user_message: Messaggio dell'utente
            user_id: ID utente per personalizzazione

        Returns:
            Risposta dell'agent
        """
        print(
            f"🔍 PROCESS_MESSAGE START: user_id='{user_id}', message='{user_message}'"
        )

        try:
            # Aggiungi user_id al context per i tools
            enhanced_message = f"[USER_ID: {user_id}] {user_message}"
            print(f"🔍 Enhanced message: '{enhanced_message}'")

            print(f"🔍 Invoking agent_with_history...")
            # Esegui agent con history automatica
            result = self.agent_with_history.invoke(
                {"input": enhanced_message},
                config={"configurable": {"session_id": user_id}},
            )
            print(f"🔍 Agent result type: {type(result)}")
            print(
                f"🔍 Agent result keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}"
            )
            print(f"🔍 Agent result: {result}")

            # Estrai output e verifica che sia presente
            output = result.get("output", "")
            print(f"🔍 Output extracted: '{output}'")
            print(f"🔍 Output length: {len(output) if output else 0}")

            # Se l'output è vuoto o contiene solo messaggi di errore tecnici
            if not output or "I'm sorry" in output or "mistake" in output:
                print(
                    "🔍 Using fallback response - output is empty or contains error messages"
                )
                fallback_result = self._fallback_response(user_message, user_id)
                print(f"🔍 Fallback result: '{fallback_result}'")
                return fallback_result

            print(f"🔍 Returning output: '{output}'")
            return output

        except Exception as e:
            print(f"❌ Error in process_message: {str(e)}")
            print(f"❌ Error type: {type(e)}")
            import traceback

            print(f"❌ Traceback: {traceback.format_exc()}")
            fallback_result = self._fallback_response(user_message, user_id)
            print(f"🔍 Fallback result after error: '{fallback_result}'")
            return fallback_result

    def _fallback_response(self, user_message: str, user_id: str) -> str:
        """
        Risposta di fallback quando l'agent ReAct fallisce
        """
        try:
            # Usa direttamente il tool di ricerca film
            db_search_tool = None
            for tool in self.tools:
                if "movie_database_search" in str(tool.name).lower():
                    db_search_tool = tool
                    break

            if db_search_tool and "tensione" in user_message.lower():
                # Cerca direttamente film di tensione
                result = db_search_tool.invoke({"query": "tensione thriller suspense"})
                return f"Ecco alcuni suggerimenti di film che potrebbero interessarti:\n\n{result}"

            return """Mi dispiace per l'inconveniente tecnico. Posso aiutarti a trovare film su Netflix! 
Prova a chiedermi:
- Film di un genere specifico (thriller, commedia, drama, etc.)
- Consigli basati sui tuoi gusti
- Informazioni su film specifici
- Ricerche per attori o registi"""

        except:
            return "Mi dispiace, sto avendo difficoltà tecniche. Riprova tra qualche istante."

    def reset_user_history(self, user_id: str) -> None:
        """Azzera la history di un utente"""
        if user_id in self._session_store:
            del self._session_store[user_id]
