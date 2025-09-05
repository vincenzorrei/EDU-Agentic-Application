/*
 * AI Chat Widget - DEBUG VERSION
 * Added extensive logging to identify the disconnection issue
 */

document.addEventListener("DOMContentLoaded", () => {
    // ================== DOM REFERENCES ==================
    const launcher = document.getElementById("chat-launcher");
    const panel = document.getElementById("chat-panel");
    const widget = document.getElementById("chat-widget");
    const closeBtn = document.getElementById("chat-close");
    const input = document.getElementById("chat-input");
    const sendBtn = document.getElementById("chat-send");
    const transcript = document.getElementById("chat-transcript");

    // Validation check for required elements
    if (!launcher || !panel || !widget || !closeBtn || !input || !sendBtn || !transcript) {
        console.error("❌ CHAT WIDGET: Elementi DOM mancanti!");
        return;
    }

    console.log("✅ Chat Widget initialized successfully");

    // ================== SESSION MANAGEMENT ==================
    const SESSION_ID = "vincenzo01";
    console.log("🧪 Using fixed SESSION_ID for testing:", SESSION_ID);

    // ================== CONFIGURATION ==================
    const WS_URL = "ws://localhost:8000/chat";
    const DEBUG_ENABLED = true;
    let websocket = null;
    let nudgeInterval = null;
    let messageBeingProcessed = false;
    let lastMessageTime = null;

    function log(...args) {
        if (DEBUG_ENABLED) {
            const timestamp = new Date().toISOString().split('T')[1].slice(0, -1);
            console.log(`[${timestamp}] [CHAT]`, ...args);
        }
    }

    // ================== DEBUG: Track all events ==================
    function debugWebSocketState() {
        if (websocket) {
            log(`📊 WebSocket State: readyState=${websocket.readyState}, bufferedAmount=${websocket.bufferedAmount}`);
        } else {
            log(`📊 WebSocket is null`);
        }
    }

    // ================== CHAT STATE MANAGEMENT ==================
    function openChat() {
        log("📂 openChat() called");
        panel.classList.add("is-open");
        widget.classList.add("open");
        launcher.setAttribute("aria-expanded", "true");
        input?.focus();
        
        // Connect WebSocket when opening chat
        connectWebSocket();
        
        log("✅ Chat opened");
    }

    function closeChat() {
        log("🚪 closeChat() called");
        log(`⚠️ Message being processed: ${messageBeingProcessed}`);
        
        // DEBUG: Check if we're processing a message
        if (messageBeingProcessed) {
            log("⚠️ WARNING: Closing chat while message is being processed!");
        }
        
        panel.classList.remove("is-open");
        widget.classList.remove("open");
        launcher.setAttribute("aria-expanded", "false");
        launcher.focus();
        
        // DEBUG: Log before closing WebSocket
        debugWebSocketState();
        
        // DON'T close WebSocket if message is being processed
        if (messageBeingProcessed) {
            log("🛑 NOT closing WebSocket - message in progress");
        } else if (websocket && websocket.readyState === WebSocket.OPEN) {
            log("❌ Closing WebSocket connection");
            websocket.close(1000, "Chat closed by user");
            websocket = null;
        }
        
        log("✅ Chat panel closed");
    }

    // ================== AUTO-RESIZE TEXTAREA ==================
    function autoResizeTextarea() {
        input.style.height = 'auto';
        const newHeight = Math.min(input.scrollHeight, 140);
        input.style.height = newHeight + 'px';
    }

    // ================== SEND BUTTON STATE ==================
    function updateSendButton() {
        const hasContent = input.value.trim().length > 0;
        sendBtn.disabled = !hasContent || messageBeingProcessed;
        sendBtn.setAttribute("aria-disabled", !hasContent || messageBeingProcessed);
    }

    // ================== MESSAGE RENDERING ==================
    function appendMessage(text, fromUser = false) {
        log(`💬 appendMessage() - fromUser: ${fromUser}, length: ${text.length}`);
        
        // Remove hint if it exists
        const hint = transcript.querySelector('.chat-hint');
        if (hint && transcript.children.length === 1) {
            hint.remove();
        }

        const wrapper = document.createElement("div");
        wrapper.className = "chat-msg" + (fromUser ? " user" : "");
        
        const bubble = document.createElement("div");
        bubble.className = "chat-bubble";
        
        if (fromUser) {
            bubble.textContent = text.trim();
        } else {
            bubble.innerHTML = renderMarkdown(text.trim());
        }
        
        wrapper.appendChild(bubble);
        transcript.appendChild(wrapper);
        transcript.scrollTop = transcript.scrollHeight;
        
        return bubble;
    }

    // ================== MARKDOWN RENDERING ==================
    function renderMarkdown(text) {
        let html = text;
        
        // Normalize markdown
        html = normalizeMarkdown(html);
        
        // Headers
        html = html.replace(/^#{6}\s+(.+)$/gm, '<h6>$1</h6>');
        html = html.replace(/^#{5}\s+(.+)$/gm, '<h5>$1</h5>');
        html = html.replace(/^#{4}\s+(.+)$/gm, '<h4>$1</h4>');
        html = html.replace(/^#{3}\s+(.+)$/gm, '<h3>$1</h3>');
        html = html.replace(/^#{2}\s+(.+)$/gm, '<h2>$1</h2>');
        html = html.replace(/^#{1}\s+(.+)$/gm, '<h1>$1</h1>');
        
        // Lists
        html = html.replace(/^\d+\.\s+(.+)$/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>)/s, '<ol>$1</ol>');
        html = html.replace(/^[-*]\s+(.+)$/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>)/s, (match) => {
            if (!match.includes('<ol>')) {
                return '<ul>' + match + '</ul>';
            }
            return match;
        });
        
        // Text formatting
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
        
        // Paragraphs
        html = html.replace(/\n\n/g, '</p><p>');
        html = '<p>' + html + '</p>';
        html = html.replace(/<p><\/p>/g, '');
        html = html.replace(/<p>\s*<\/p>/g, '');
        
        return html;
    }

    function normalizeMarkdown(text) {
        text = text.replace(/([.!?])([A-Z#])/g, '$1\n\n$2');
        text = text.replace(/([a-z])(\d+\.)/g, '$1\n\n$2');
        text = text.replace(/([a-z])(#{1,6}\s)/g, '$1\n\n$2');
        return text;
    }

    // ================== TYPING EFFECT ==================
    function simulateTypingEffect(element, text, speed = 6) {
        log(`⌨️ Starting typing effect for ${text.length} characters`);
        element.textContent = "";
        let i = 0;
        
        const typeInterval = setInterval(() => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                transcript.scrollTop = transcript.scrollHeight;
            } else {
                clearInterval(typeInterval);
                const normalized = normalizeMarkdown(text);
                element.innerHTML = renderMarkdown(normalized);
                transcript.scrollTop = transcript.scrollHeight;
                
                // Message processing complete
                log("✅ Typing effect complete, setting messageBeingProcessed = false");
                messageBeingProcessed = false;
                updateSendButton();
            }
        }, speed);
        
        return typeInterval;
    }

    // ================== WEBSOCKET COMMUNICATION ==================
    function connectWebSocket() {
        log("🔌 connectWebSocket() called");
        debugWebSocketState();
        
        if (websocket && websocket.readyState === WebSocket.OPEN) {
            log("✅ WebSocket already connected");
            return;
        }

        const wsUrl = `${WS_URL}/${SESSION_ID}`;
        log(`🔌 Creating new WebSocket connection to: ${wsUrl}`);

        websocket = new WebSocket(wsUrl);

        websocket.onopen = function(event) {
            log("✅ WebSocket.onopen fired");
            debugWebSocketState();
        };

        websocket.onmessage = function(event) {
            const responseTime = Date.now() - lastMessageTime;
            log(`📨 WebSocket.onmessage fired (response time: ${responseTime}ms)`);
            log(`📨 Message length: ${event.data.length}`);
            debugWebSocketState();

            // Add bot response with typing effect
            const botBubble = appendMessage("", false);
            simulateTypingEffect(botBubble, event.data);
        };

        websocket.onclose = function(event) {
            log(`🔴 WebSocket.onclose fired - Code: ${event.code}, Reason: "${event.reason}"`);
            log(`🔴 Clean close: ${event.wasClean}`);
            debugWebSocketState();
            
            // Analyze close reason
            if (event.code === 1000) {
                log("🔴 Normal closure (1000)");
            } else if (event.code === 1006) {
                log("🔴 Abnormal closure (1006) - connection lost");
            } else {
                log(`🔴 Unexpected close code: ${event.code}`);
            }
            
            websocket = null;
            messageBeingProcessed = false;
            updateSendButton();
        };

        websocket.onerror = function(error) {
            log("❌ WebSocket.onerror fired:", error);
            debugWebSocketState();
            appendMessage("Sorry, I'm having trouble connecting. Please try again.", false);
        };
    }

    async function sendMessage(message) {
        const trimmed = message.trim();
        if (!trimmed) return;

        log(`📤 sendMessage() called with: "${trimmed}"`);
        lastMessageTime = Date.now();
        messageBeingProcessed = true;

        // Add user message
        appendMessage(trimmed, true);

        // Clear input
        input.value = "";
        updateSendButton();
        autoResizeTextarea();

        try {
            // Connect WebSocket if needed
            if (!websocket || websocket.readyState !== WebSocket.OPEN) {
                log("⚠️ WebSocket not open, connecting...");
                connectWebSocket();
                
                // Wait for connection
                await new Promise((resolve, reject) => {
                    const timeout = setTimeout(() => {
                        log("❌ WebSocket connection timeout");
                        reject(new Error("Connection timeout"));
                    }, 5000);
                    
                    const checkInterval = setInterval(() => {
                        if (websocket && websocket.readyState === WebSocket.OPEN) {
                            clearTimeout(timeout);
                            clearInterval(checkInterval);
                            log("✅ WebSocket connected, ready to send");
                            resolve();
                        }
                    }, 100);
                });
            }

            // Send message via WebSocket
            log(`📤 Sending message via WebSocket...`);
            debugWebSocketState();
            websocket.send(trimmed);
            log(`✅ Message sent successfully`);

        } catch (error) {
            log("❌ Send error:", error);
            appendMessage("Sorry, I'm having trouble connecting. Please try again.", false);
            messageBeingProcessed = false;
            updateSendButton();
        }
    }

    // ================== INPUT VALIDATION ==================
    function validateAndSend() {
        log("🎯 validateAndSend() called");
        const message = input.value.trim();
        
        if (!message) {
            const composer = document.querySelector('.chat-composer');
            composer.classList.add('shake');
            setTimeout(() => composer.classList.remove('shake'), 400);
            return;
        }

        if (message.length > 2000) {
            appendMessage("Message too long. Please keep it under 2000 characters.", false);
            return;
        }

        sendMessage(message);
    }

    // ================== EVENT LISTENERS ==================
    
    // Launcher click
    launcher.addEventListener("click", () => {
        log("🎯 Launcher clicked");
        openChat();
    });

    // Close button click
    closeBtn.addEventListener("click", () => {
        log("🎯 Close button clicked");
        closeChat();
    });

    // Send button click
    sendBtn.addEventListener("click", () => {
        log("🎯 Send button clicked");
        validateAndSend();
    });

    // Input events
    input.addEventListener("input", () => {
        updateSendButton();
        autoResizeTextarea();
    });

    // Enter key to send
    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            log("🎯 Enter key pressed");
            e.preventDefault();
            validateAndSend();
        }
    });

    // Escape key to close
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && widget.classList.contains("open")) {
            log("🎯 Escape key pressed");
            closeChat();
        }
    });

    // DEBUG: Track page visibility
    document.addEventListener("visibilitychange", () => {
        log(`👁️ Page visibility changed: ${document.hidden ? 'HIDDEN' : 'VISIBLE'}`);
    });

    // DEBUG: Track window focus
    window.addEventListener("focus", () => log("🎯 Window FOCUSED"));
    window.addEventListener("blur", () => log("😴 Window BLURRED"));

    // DEBUG: Intercept beforeunload
    window.addEventListener("beforeunload", (e) => {
        log("⚠️ beforeunload event fired!");
        if (messageBeingProcessed) {
            log("⚠️ WARNING: Page unloading while message is being processed!");
        }
        // This should only fire when actually leaving the page
        if (websocket && websocket.readyState === WebSocket.OPEN) {
            websocket.close(1000, "Page unload");
        }
    });

    // DEBUG: Track any click on page
    document.addEventListener("click", (e) => {
        if (!widget.contains(e.target)) {
            log(`🎯 Click outside widget on: ${e.target.tagName}.${e.target.className}`);
        }
    });

    // ================== INITIALIZATION ==================
    
    updateSendButton();
    
    log("🚀 Chat Widget fully initialized");
    log(`🔧 Debug mode: ENABLED`);
    log(`👤 Session ID: ${SESSION_ID}`);
});