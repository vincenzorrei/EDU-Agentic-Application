# Netflix AI Chat Assistant

Un chatbot intelligente per la scoperta di film Netflix, sviluppato con LangChain e tecnologie AI avanzate. Il sistema combina un database interno di film Netflix con ricerche web per fornire raccomandazioni personalizzate e informazioni dettagliate sui film.

## 🚀 Caratteristiche Principali

- **Raccomandazioni Personalizzate**: Sistema di raccomandazioni basato su conversazioni precedenti
- **Ricerca Semantica**: Ricerca intelligente nel database film utilizzando descrizioni e metadata
- **Integrazione Web**: Ricerche su Reddit e fonti web per opinioni della community
- **Interfaccia Moderna**: Chat widget responsive con design Netflix-style
- **Memory Conversazionale**: Mantiene il contesto delle conversazioni per personalizzazione

## 🏗️ Architettura Tecnica

### Backend
- **LangChain Agent**: Orchestratore principale con 3 tools specializzati
- **Vector Database**: FAISS per ricerca semantica su film e conversazioni utenti
- **WebSocket**: Comunicazione real-time tra frontend e backend
- **FastAPI**: Framework web moderno per API REST e WebSocket

### Frontend
- **Vanilla JavaScript**: Chat widget leggero e performante
- **Responsive Design**: Ottimizzato per desktop e mobile
- **Markdown Support**: Rendering di testo formattato nelle risposte
- **Session Management**: Gestione automatica delle sessioni utente

## 📋 Prerequisiti

- Python 3.8+
- Node.js 14+ (per il server di sviluppo frontend)
- API Keys per:
  - OpenAI (per il modello LLM)
  - Tavily (per ricerche web)
  - Reddit (per opinioni community)

## 🛠️ Installazione

### 1. Clona il Repository

```bash
git clone <repository-url>
cd EDU-Agentic-Application
```

### 2. Configura l'Ambiente Python

```bash
# Crea ambiente virtuale
python -m venv .venv

# Attiva ambiente virtuale
# Su Windows:
.venv\Scripts\activate
# Su macOS/Linux:
source .venv/bin/activate

# Installa dipendenze
pip install -r requirements.txt
```

### 3. Configura le Variabili d'Ambiente

Crea un file `.env` nella cartella `backend/` con le seguenti variabili:

```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
REDDIT_USER_AGENT=your_app_name/1.0
```

## 🚀 Avvio dell'Applicazione

### 1. Avvia il Backend

```bash
cd backend
python main.py
```

Il backend sarà disponibile su:
- **WebSocket**: `ws://localhost:8000/chat/{user_id}`
- **Health Check**: `http://localhost:8000/health`
- **API Docs**: `http://localhost:8000/docs`

### 2. Avvia il Frontend

Apri il file `frontend/index.html` nel tuo browser preferito, oppure usa un server di sviluppo:

```bash
# Opzione 1: Apri direttamente nel browser
# Naviga a: file:///path/to/frontend/index.html

# Opzione 2: Server di sviluppo (opzionale)
cd frontend
python -m http.server 3000
# Poi apri: http://localhost:3000
```

## 💬 Come Utilizzare

1. **Apri la Chat**: Clicca sul pulsante "Netflix Chat" in basso a destra
2. **Inizia la Conversazione**: Scrivi domande come:
   - "Voglio un thriller psicologico"
   - "Com'è Inception?"
   - "Qualcosa come Interstellar"
   - "È adatto ai bambini?"

3. **Personalizzazione**: Il sistema ricorda le tue preferenze per raccomandazioni future

## 🔧 Struttura del Progetto

```
EDU-Agentic-Application/
├── backend/
│   ├── agent/                 # LangChain Agent
│   ├── database/              # Vector Database e Data
│   ├── tools/                 # Tools specializzati
│   ├── utils/                 # Utility e Prompts
│   ├── main.py               # Server FastAPI
│   └── config.py             # Configurazione
├── frontend/
│   ├── images/               # Assets grafici
│   ├── index.html            # Pagina principale
│   ├── style.css             # Stili CSS
│   └── chat-widget.js        # Widget JavaScript
└── requirements.txt          # Dipendenze Python
```

## 🛠️ Tools Disponibili

### 1. Movie Database Search
- Ricerca semantica nel database film Netflix
- Filtri per disponibilità (incluso/noleggio/non disponibile)
- Link Netflix integrati

### 2. Web Movie Research
- Ricerche su Reddit per opinioni community
- Analisi critica tramite Tavily
- Sintesi intelligente senza spoiler

### 3. User History Tool
- Recupero conversazioni precedenti
- Personalizzazione basata su preferenze
- Context-aware recommendations

## 🔍 Troubleshooting

### Problemi Comuni

**Backend non si avvia:**
- Verifica che tutte le API keys siano configurate correttamente
- Controlla che la porta 8000 sia libera
- Assicurati che l'ambiente virtuale sia attivato

**Frontend non si connette:**
- Verifica che il backend sia in esecuzione
- Controlla la console del browser per errori
- Assicurati che il WebSocket sia accessibile

**Errori di memoria:**
- Il sistema usa FAISS in-memory, riavvia il backend se necessario
- Controlla i log per errori di vector store

## 📊 Performance

- **Latenza**: < 2 secondi per risposta tipica
- **Concorrenza**: Supporta multiple sessioni simultanee
- **Memoria**: ~200MB per il vector store in memoria
- **Scalabilità**: Architettura modulare per espansioni future

## 🤝 Contributi

1. Fork del repository
2. Crea un branch per la feature (`git checkout -b feature/AmazingFeature`)
3. Commit delle modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📄 Licenza

Questo progetto è sviluppato per scopi educativi nell'ambito del corso Develhope.

## 🆘 Supporto

Per problemi o domande:
- Controlla la sezione Troubleshooting
- Verifica i log del backend per errori dettagliati
- Apri una issue su GitHub per bug o feature requests

---

**Sviluppato con ❤️ per Develhope**
