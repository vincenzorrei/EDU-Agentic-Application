# Specifiche Tecniche Chat Widget

## Panoramica
Widget di chat AI integrato in un portfolio web con supporto per desktop e mobile, caratterizzato da design moderno con tema brand #7a0405 (rosso scuro) e interfaccia conversazionale completa.

## Struttura DOM

### Contenitore Principale
```html
<div id="chat-widget" aria-live="polite">
```
- Posizionamento: `position: fixed; right: 24px; bottom: 24px; z-index: 9999`
- Responsive: mobile `right: 8px; bottom: 8px`

### Launcher (Pulsante di Apertura)
```html
<button class="chat-launcher" id="chat-launcher" aria-label="Open chat with Joi" aria-expanded="false" type="button">
    <div class="launcher-icon" aria-hidden="true">
        <svg width="22" height="22" viewBox="0 0 24 24">
            <path fill="currentColor" d="M4 4h16v11a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/>
        </svg>
    </div>
    <div class="launcher-text">
        <span class="launcher-title">Chat with Joi</span>
        <span class="launcher-subtitle">My AI Assistant</span>
    </div>
</button>
```

**Specifiche di Stile:**
- Forma: pillola con `border-radius: 9999px`
- Dimensioni: `height: 50px; width: fit-content`
- Background: `linear-gradient(90deg, #7a0405, #450707)`
- Padding asimmetrico: `12px 24px 12px 16px`
- Icona circolare: 28x28px con background `#7a0405`
- Typography: title 13px/600, subtitle 10px con opacità 85%

**Effetti Interattivi:**
- Hover: `translateY(-2px)` + gradient più chiaro + glow intensificato
- Focus: outline bianco 4px
- Animazione "nudge" ogni 5 secondi quando chiuso
- Nascosto quando pannello aperto: `#chat-widget.open .chat-launcher { display:none; }`

### Pannello Chat
```html
<section class="chat-panel" id="chat-panel" role="dialog" aria-modal="true" aria-labelledby="chat-title" aria-describedby="chat-desc">
```

**Dimensioni e Layout:**
- Desktop: `380px x 560px`
- Mobile: full-screen con `calc(100vh - 120px)` height
- Border-radius: 16px
- Display: `flex-direction: column`

**Stati:**
- Chiuso: `display: none`
- Aperto: `display: flex` + animazione `chatIn` (0.22s cubic-bezier)
- Transform-origin: `100% 100%` (da angolo bottom-right)

### Header del Pannello
```html
<header class="chat-header">
    <div class="chat-title">
        <h3 id="chat-title">Joi - AI Assistant</h3>
        <span class="badge" id="chat-desc">Secure - GDPR Ready</span>
    </div>
    <button class="chat-close" id="chat-close" aria-label="Close chat" type="button">
        <svg>...</svg>
    </button>
</header>
```

**Specifiche:**
- Padding: `14px 14px 8px`
- Background: `var(--chat-surface)`
- Border-bottom: `1px solid var(--chat-border)`
- Badge: pillola con border e padding `2px 8px`
- Close button: 36x36px con hover subtle

### Area Messaggi (Transcript)
```html
<div class="chat-transcript" id="chat-transcript">
    <div class="chat-hint">Tell me about your project or ask for use cases.</div>
</div>
```

**Layout Messaggi:**
- Container: `padding: 12px; overflow-y: auto; flex: 1`
- Messaggio utente: `justify-content: flex-end`
- Messaggio bot: align left, background transparent
- Margine tra messaggi: `30px 0`

**Bubble Styling:**
- Utente: background `var(--chat-accent)` + colore brand
- Bot: background transparent, no borders, full-width
- Typography: `font-size: 14px; line-height: 1.5`
- Padding utente: `2px 12px`
- Padding bot: `0` (solo `padding-left: 10px` per indentazione)

### Composer (Input Area)
```html
<div class="chat-composer">
    <textarea id="chat-input" rows="1" placeholder="Type your question…" maxlength="2000"></textarea>
    <div class="chat-actions">
        <button class="chat-send" id="chat-send" type="button" aria-label="Send message">
            <svg>...</svg>
        </button>
    </div>
</div>
```

**Grid Layout:**
- Display: `grid; grid-template-columns: 1fr auto; gap: 10px`
- Textarea: auto-resize, `max-height: 140px; min-height: 40px`
- Send button: 46x46px circolare, disabilitato se input vuoto

## Variabili CSS (Tema)

```css
:root {
    --chat-bg: #ffffff;
    --chat-surface: #f7f9fb;
    --chat-border: #e2e8f0;
    --chat-text: #1a1f24;
    --chat-subtle: #64707d;
    --chat-accent: #7a0405;
    --chat-accent-text: #ffffff;
    --chat-shadow: 0 8px 28px rgba(0,0,0,.12);
}
```

## Funzionalità JavaScript

### Inizializzazione
```javascript
document.addEventListener("DOMContentLoaded", () => {
    // Riferimenti DOM obbligatori
    const launcher = document.getElementById("chat-launcher");
    const panel = document.getElementById("chat-panel");
    const widget = document.getElementById("chat-widget");
    // ... altri elementi
    
    // Validazione esistenza elementi
    if (!launcher || !panel || !widget) {
        console.error("❌ CHAT WIDGET: Elementi DOM mancanti!");
        return;
    }
});
```

### Gestione Sessione
```javascript
const SESSION_ID = (() => {
    let s = localStorage.getItem("sid");
    if (!s) {
        s = (crypto?.randomUUID?.() || String(Date.now()));
        localStorage.setItem("sid", s);
    }
    return s;
})();
```

### Apertura/Chiusura
```javascript
function openChat() {
    panel.classList.add("is-open");
    widget.classList.add("open");
    launcher.setAttribute("aria-expanded", "true");
    input?.focus();
}

function closeChat() {
    panel.classList.remove("is-open");
    widget.classList.remove("open");
    launcher.setAttribute("aria-expanded", "false");
    launcher.focus();
}
```

**Event Listeners:**
- Click launcher → openChat
- Click close button → closeChat
- Escape key → closeChat (se aperto)

### Rendering Messaggi

**Creazione Messaggi:**
```javascript
function appendMessage(text, fromUser = false) {
    const wrapper = document.createElement("div");
    wrapper.className = "chat-msg" + (fromUser ? " user" : "");
    const bubble = document.createElement("div");
    bubble.className = "chat-bubble";
    bubble.innerHTML = renderMarkdown(text.trim());
    wrapper.appendChild(bubble);
    transcript.appendChild(wrapper);
    transcript.scrollTop = transcript.scrollHeight;
}
```

**Markdown Rendering:**
- Headings: `#{1,6}` → `<h1-6>`
- Liste numerate: `1. 2. 3.` → `<ol><li>`
- Liste bullet: `- *` → `<ul><li>`
- Text formatting: **bold**, *italic*
- Gestione liste speciali con pattern `:number` e `:-`
- Normalizzazione per streaming: separazione automatica elementi attaccati

### Comunicazione API

**Configurazione:**
```javascript
const API_BASE = "/api";  // Proxy Netlify
const requestBody = {
    tenant_id: "default",
    session_id: SESSION_ID,
    messages: [{ role: "user", content: trimmed }],
};
```

**Invio Non-Streaming:**
```javascript
const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(requestBody),
    signal: abortController.signal,  // 120s timeout
});

const responseData = await res.json();
const responseText = responseData.content || responseData.message || responseData.text;
```

**Effetto Typing Simulato:**
```javascript
function simulateTypingEffect(element, text, speed = 6) {
    element.textContent = "";
    let i = 0;
    
    const typeInterval = setInterval(() => {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            transcript.scrollTop = transcript.scrollHeight;
        } else {
            clearInterval(typeInterval);
            const norm = normalizeMarkdown(text);
            element.innerHTML = renderMarkdown(norm);
        }
    }, speed);
}
```

### UX Features

**Validazione Input:**
- Stato send button aggiornato on input
- Shake animation per input invalido
- Focus automatico su apertura
- Max-length: 2000 caratteri

**Nudge Animation:**
- Intervallo: 5 secondi
- Solo quando chat chiusa e pagina visibile
- Keyframes: `translateY(-4px) scale(1.05)` con box-shadow intensificato

**Mobile Optimizations:**
- Visual Viewport API per gestione tastiera
- Altezza dinamica: `calc(100vh - 60px)` con tastiera
- Classe `keyboard-active` per stili specifici
- Fallback resize listener per browser legacy

## Responsive Design

**Breakpoint Mobile: 640px**

**Pannello Mobile:**
```css
.chat-panel {
    position: fixed;
    bottom: 8px; left: 8px; right: 8px;
    width: auto;
    height: calc(100vh - 120px);
    max-height: calc(100vh - 16px);
    min-height: 400px;
}
```

**Gestione Tastiera Mobile:**
```css
.chat-panel.keyboard-active {
    border-radius: 16px 16px 0 0 !important;
    transition: height 0.3s ease, max-height 0.3s ease;
}
```

**Media Queries Specifiche:**
- Standard mobile: max-width 640px
- Tastiera attiva: max-height 500px
- Reduced motion: disabilita tutte le animazioni

## Accessibilità

**ARIA Labels:**
- Launcher: `aria-label="Open chat with Joi" aria-expanded="false"`
- Panel: `role="dialog" aria-modal="true" aria-labelledby="chat-title"`
- Close: `aria-label="Close chat"`
- Send: `aria-label="Send message"`

**Keyboard Navigation:**
- Tab order: launcher → input → send → close
- Enter nel textarea: invio messaggio (preventDefault su shift+enter)
- Escape: chiusura chat
- Focus management: apertura → input focus, chiusura → launcher focus

**Screen Reader:**
- Live region: `aria-live="polite"` sul contenitore
- SVG decorative: `aria-hidden="true"`
- Disabled state: `aria-disabled` su send button

## Configurazioni di Deploy

**Netlify Proxy Configuration:**
```toml
[[redirects]]
  from = "/api/*"
  to = "https://web-production-63073.up.railway.app/:splat"
  status = 200
  force = true
  [redirects.headers]
    Authorization = "Bearer [TOKEN]"
    X-Accel-Buffering = "no"
    Cache-Control = "no-cache, no-store, must-revalidate"
```

**Timeout Management:**
- Frontend: 120 secondi (AbortController)
- Backend: gestito da Railway
- Fallback: messaggi di errore user-friendly

## Note Implementative

1. **Graceful Degradation:** Widget si disabilita se elementi DOM mancanti
2. **Debug Mode:** Console logging configurabile via `DEBUG_ENABLED`
3. **Session Persistence:** localStorage con fallback a timestamp
4. **Error Handling:** Gestione CORS, timeout, network failures
5. **Performance:** Event listeners singoli, cleanup automatico animazioni
6. **Cross-browser:** Fallback per crypto.randomUUID, Visual Viewport API

Questo widget è progettato per integrazione seamless in qualsiasi frontend moderno mantenendo design consistency e UX ottimale su tutti i dispositivi.
