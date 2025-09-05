/*
 * AI Chat Widget - Full Implementation
 * Following specifications from chat_widget.md
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
    // 🧪 TEST: Usa ID fisso semplice invece di UUID lungo
    const SESSION_ID = "010101";
    console.log("🧪 Using fixed SESSION_ID for testing:", SESSION_ID);

    // ================== CONFIGURATION ==================
    const WS_URL = "ws://localhost:8000/chat"; // WebSocket backend URL
    const DEBUG_ENABLED = true;
    let websocket = null;
    let nudgeInterval = null;

    function log(...args) {
        if (DEBUG_ENABLED) {
            console.log("[CHAT WIDGET]", ...args);
        }
    }

    // ================== CHAT STATE MANAGEMENT ==================
    function openChat() {
        panel.classList.add("is-open");
        widget.classList.add("open");
        launcher.setAttribute("aria-expanded", "true");
        input?.focus();
        
        // Clear hint message when opening
        const hint = transcript.querySelector('.chat-hint');
        if (hint && transcript.children.length === 1) {
            // Keep hint if it's the only element
        }
        
        // Connect WebSocket when opening chat
        connectWebSocket();
        
        log("Chat opened");
    }

    function closeChat() {
        panel.classList.remove("is-open");
        widget.classList.remove("open");
        launcher.setAttribute("aria-expanded", "false");
        launcher.focus();
        
        // Close WebSocket connection immediatamente
        if (websocket && websocket.readyState === WebSocket.OPEN) {
            websocket.close(1000, "Chat closed by user");
            websocket = null;
        }
        
        log("Chat closed");
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
        sendBtn.disabled = !hasContent;
        sendBtn.setAttribute("aria-disabled", !hasContent);
    }

    // ================== MESSAGE RENDERING ==================
    function appendMessage(text, fromUser = false) {
        // Remove hint if it exists and this is the first real message
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
        
        return bubble; // Return for typing effect
    }

    // ================== MARKDOWN RENDERING ==================
    function renderMarkdown(text) {
        let html = text;
        
        // Normalize markdown for better parsing
        html = normalizeMarkdown(html);
        
        // Headers (must be at start of line)
        html = html.replace(/^#{6}\s+(.+)$/gm, '<h6>$1</h6>');
        html = html.replace(/^#{5}\s+(.+)$/gm, '<h5>$1</h5>');
        html = html.replace(/^#{4}\s+(.+)$/gm, '<h4>$1</h4>');
        html = html.replace(/^#{3}\s+(.+)$/gm, '<h3>$1</h3>');
        html = html.replace(/^#{2}\s+(.+)$/gm, '<h2>$1</h2>');
        html = html.replace(/^#{1}\s+(.+)$/gm, '<h1>$1</h1>');
        
        // Numbered lists
        html = html.replace(/^\d+\.\s+(.+)$/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>)/s, '<ol>$1</ol>');
        
        // Bullet lists
        html = html.replace(/^[-*]\s+(.+)$/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>)/s, (match) => {
            if (!match.includes('<ol>')) {
                return '<ul>' + match + '</ul>';
            }
            return match;
        });
        
        // Special list patterns
        html = html.replace(/^:\d+\s+(.+)$/gm, '<li>$1</li>');
        html = html.replace(/^:-\s+(.+)$/gm, '<li>$1</li>');
        
        // Text formatting
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
        
        // Paragraphs
        html = html.replace(/\n\n/g, '</p><p>');
        html = '<p>' + html + '</p>';
        
        // Clean up empty paragraphs
        html = html.replace(/<p><\/p>/g, '');
        html = html.replace(/<p>\s*<\/p>/g, '');
        
        return html;
    }

    function normalizeMarkdown(text) {
        // Separate elements that are stuck together
        text = text.replace(/([.!?])([A-Z#])/g, '$1\n\n$2');
        text = text.replace(/([a-z])(\d+\.)/g, '$1\n\n$2');
        text = text.replace(/([a-z])(#{1,6}\s)/g, '$1\n\n$2');
        
        return text;
    }

    // ================== TYPING EFFECT ==================
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
                // Replace with properly formatted markdown
                const normalized = normalizeMarkdown(text);
                element.innerHTML = renderMarkdown(normalized);
                transcript.scrollTop = transcript.scrollHeight;
            }
        }, speed);
        
        return typeInterval;
    }

    // ================== WEBSOCKET COMMUNICATION ==================
    function connectWebSocket() {
        if (websocket && websocket.readyState === WebSocket.OPEN) {
            return; // Already connected
        }

        // Usa SESSION_ID dinamico per ogni utente/sessione
        const wsUrl = `${WS_URL}/${SESSION_ID}`;
        log("Connecting to WebSocket:", wsUrl);

        websocket = new WebSocket(wsUrl);

        websocket.onopen = function() {
            log("WebSocket connected successfully");
        };

        websocket.onmessage = function(event) {
            const response = event.data;
            log("WebSocket response:", response);
            log("WebSocket state after message:", websocket.readyState);

            // Add bot response with typing effect
            const botBubble = appendMessage("", false);
            simulateTypingEffect(botBubble, response);
            
            log("After adding message, WebSocket state:", websocket.readyState);
        };

        websocket.onclose = function(event) {
            log("WebSocket closed:", event.code, event.reason);
            log("WebSocket state at close:", websocket.readyState);
            
            // Gestisci diversi codici di chiusura
            if (event.code === 1006) {
                log("⚠️ Connessione chiusa inaspettatamente");
                // Potrebbe essere necessario riconnettere
            } else if (event.code === 1000) {
                log("✅ Connessione chiusa normalmente");
            }
            
            websocket = null;
        };

        websocket.onerror = function(error) {
            log("WebSocket error:", error);
            appendMessage("Sorry, I'm having trouble connecting. Please try again.", false);
        };
    }

    async function sendMessage(message) {
        const trimmed = message.trim();
        if (!trimmed) return;

        log("Sending message:", trimmed);

        // Add user message
        appendMessage(trimmed, true);

        // Clear input
        input.value = "";
        updateSendButton();
        autoResizeTextarea();

        // Disable send button during request
        sendBtn.disabled = true;

        try {
            // Connect WebSocket if needed
            if (!websocket || websocket.readyState !== WebSocket.OPEN) {
                connectWebSocket();
                
                // Wait for connection
                await new Promise((resolve, reject) => {
                    const timeout = setTimeout(() => reject(new Error("Connection timeout")), 5000);
                    
                    if (websocket.readyState === WebSocket.OPEN) {
                        clearTimeout(timeout);
                        resolve();
                        return;
                    }
                    
                    websocket.onopen = () => {
                        clearTimeout(timeout);
                        resolve();
                    };
                    
                    websocket.onerror = () => {
                        clearTimeout(timeout);
                        reject(new Error("Connection failed"));
                    };
                });
            }

            // Send message via WebSocket
            websocket.send(trimmed);

        } catch (error) {
            log("Send error:", error);
            appendMessage("Sorry, I'm having trouble connecting. Please try again.", false);
        } finally {
            sendBtn.disabled = false;
            updateSendButton();
        }
    }

    // ================== INPUT VALIDATION ==================
    function validateAndSend() {
        const message = input.value.trim();
        
        if (!message) {
            // Shake animation for empty input
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

    // ================== NUDGE ANIMATION ==================
    function startNudgeAnimation() {
        // Only nudge if chat is closed and page is visible
        if (!document.hidden && !widget.classList.contains('open')) {
            launcher.classList.add('nudge');
            setTimeout(() => launcher.classList.remove('nudge'), 600);
        }
    }

    function setupNudging() {
        // Clear existing interval
        if (nudgeInterval) {
            clearInterval(nudgeInterval);
        }
        
        // Only start nudging if chat is closed
        if (!widget.classList.contains('open')) {
            nudgeInterval = setInterval(startNudgeAnimation, 5000);
        }
    }

    function stopNudging() {
        if (nudgeInterval) {
            clearInterval(nudgeInterval);
            nudgeInterval = null;
        }
        launcher.classList.remove('nudge');
    }

    // ================== MOBILE KEYBOARD HANDLING ==================
    function setupMobileKeyboardHandling() {
        if ('visualViewport' in window) {
            function handleViewportChange() {
                const viewport = window.visualViewport;
                const heightDiff = window.innerHeight - viewport.height;
                
                if (heightDiff > 150) { // Keyboard is likely open
                    panel.classList.add('keyboard-active');
                    panel.style.height = `calc(${viewport.height}px - 60px)`;
                } else {
                    panel.classList.remove('keyboard-active');
                    panel.style.height = '';
                }
            }
            
            window.visualViewport.addEventListener('resize', handleViewportChange);
            window.visualViewport.addEventListener('scroll', handleViewportChange);
        } else {
            // Fallback for older browsers
            window.addEventListener('resize', () => {
                if (window.innerHeight < 500 && panel.classList.contains('is-open')) {
                    panel.classList.add('keyboard-active');
                } else {
                    panel.classList.remove('keyboard-active');
                }
            });
        }
    }

    // ================== EVENT LISTENERS ==================
    
    // Launcher click
    launcher.addEventListener("click", () => {
        openChat();
        stopNudging();
    });

    // Close button click
    closeBtn.addEventListener("click", closeChat);

    // Send button click
    sendBtn.addEventListener("click", validateAndSend);

    // Input events
    input.addEventListener("input", () => {
        updateSendButton();
        autoResizeTextarea();
    });

    // Enter key to send (but not Shift+Enter)
    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            validateAndSend();
        }
    });

    // Keyboard navigation
    document.addEventListener("keydown", (e) => {
        // Escape to close chat
        if (e.key === "Escape" && widget.classList.contains("open")) {
            closeChat();
        }
        
        // Tab navigation management
        if (e.key === "Tab" && widget.classList.contains("open")) {
            const focusableElements = panel.querySelectorAll(
                'input, textarea, button, [tabindex]:not([tabindex="-1"])'
            );
            const firstElement = focusableElements[0];
            const lastElement = focusableElements[focusableElements.length - 1];
            
            if (e.shiftKey && document.activeElement === firstElement) {
                e.preventDefault();
                lastElement.focus();
            } else if (!e.shiftKey && document.activeElement === lastElement) {
                e.preventDefault();
                firstElement.focus();
            }
        }
    });

    // Visibility change handling for nudging
    document.addEventListener("visibilitychange", () => {
        if (document.hidden) {
            stopNudging();
        } else {
            setupNudging();
        }
    });

    // ================== INITIALIZATION ==================
    
    // Set initial send button state
    updateSendButton();
    
    // Setup mobile keyboard handling
    setupMobileKeyboardHandling();
    
    // Start nudge animation
    setupNudging();
    
    // Add welcome message after a short delay
    setTimeout(() => {
        log("Chat widget ready for interactions");
    }, 500);

    log("Chat Widget fully initialized with session:", SESSION_ID);
});