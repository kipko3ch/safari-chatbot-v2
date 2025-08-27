// Safari Chat Widget Embed Script
(function() {
    // Create and inject the chat widget HTML
    const chatWidgetHTML = `
        <div id="safari-chat-widget" style="position: fixed; bottom: 20px; right: 20px; z-index: 10000; font-family: Arial, sans-serif;">
            <!-- Chat Toggle Button -->
            <div id="chat-toggle" style="width: 60px; height: 60px; background: linear-gradient(135deg, #ff6b35, #f7931e); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.15); transition: transform 0.2s;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
            </div>

            <!-- Chat Window -->
            <div id="chat-window" style="position: absolute; bottom: 80px; right: 0; width: 350px; height: 500px; background: white; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); display: none; flex-direction: column; overflow: hidden;">
                <!-- Chat Header -->
                <div style="background: linear-gradient(135deg, #ff6b35, #f7931e); color: white; padding: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: bold; font-size: 16px;">Safari Assistant</div>
                        <div style="font-size: 12px; opacity: 0.9;">Nature Warriors African Safaris</div>
                    </div>
                    <div id="chat-close" style="cursor: pointer; font-size: 20px;">×</div>
                </div>

                <!-- Chat Messages -->
                <div id="chat-messages" style="flex: 1; padding: 15px; overflow-y: auto; background: #f8f9fa;">
                    <!-- Welcome message -->
                    <div style="margin-bottom: 15px;">
                        <div style="background: linear-gradient(135deg, #e3f2fd, #f3e5f5); padding: 15px; border-radius: 12px; font-size: 14px; border-left: 4px solid #ff6b35;">
                            <div style="font-weight: bold; margin-bottom: 8px; color: #1976d2;">🌟 Welcome to Nature Warriors!</div>
                            <div>Hi there! I'm your personal safari assistant. I'd love to help you discover the magic of Tanzania! What adventure are you dreaming of today?</div>
                        </div>
                    </div>
                </div>

                <!-- Quick Suggestions -->
                <div id="quick-suggestions" style="padding: 15px; background: #f8f9fa; border-top: 1px solid #e9ecef;">
                    <div style="font-size: 12px; color: #666; margin-bottom: 8px;">💡 Quick questions:</div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <button class="suggestion-btn" style="background: white; border: 1px solid #dee2e6; padding: 8px 12px; border-radius: 20px; font-size: 12px; cursor: pointer; transition: all 0.2s;">🦁 Serengeti Safari</button>
                        <button class="suggestion-btn" style="background: white; border: 1px solid #dee2e6; padding: 8px 12px; border-radius: 20px; font-size: 12px; cursor: pointer; transition: all 0.2s;">🏔️ Kilimanjaro Trek</button>
                        <button class="suggestion-btn" style="background: white; border: 1px solid #dee2e6; padding: 8px 12px; border-radius: 20px; font-size: 12px; cursor: pointer; transition: all 0.2s;">🏝️ Zanzibar Beach</button>
                        <button class="suggestion-btn" style="background: white; border: 1px solid #dee2e6; padding: 8px 12px; border-radius: 20px; font-size: 12px; cursor: pointer; transition: all 0.2s;">📞 Contact Us</button>
                    </div>
                </div>

                <!-- Chat Input -->
                <div style="padding: 15px; background: white; border-top: 1px solid #e9ecef;">
                    <div style="display: flex; gap: 10px;">
                        <input type="text" id="chat-input" placeholder="Type your message..." style="flex: 1; padding: 10px; border: 1px solid #dee2e6; border-radius: 20px; outline: none; font-size: 14px;">
                        <button id="chat-send" style="background: #ff6b35; color: white; border: none; padding: 10px 15px; border-radius: 20px; cursor: pointer; font-size: 14px;">Send</button>
                    </div>
                </div>
            </div>

            <!-- Notification Badge -->
            <div id="notification-badge" style="position: absolute; top: -5px; right: -5px; background: #ff4757; color: white; border-radius: 50%; width: 20px; height: 20px; display: none; align-items: center; justify-content: center; font-size: 12px; font-weight: bold;">1</div>
        </div>
    `;

    // Inject the HTML into the page
    document.body.insertAdjacentHTML('beforeend', chatWidgetHTML);

    // Get DOM elements
    const chatToggle = document.getElementById('chat-toggle');
    const chatWindow = document.getElementById('chat-window');
    const chatClose = document.getElementById('chat-close');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    const quickSuggestions = document.getElementById('quick-suggestions');
    const notificationBadge = document.getElementById('notification-badge');

    let isOpen = false;

    // API server URL
    const apiServerUrl = 'https://safari-chatbot-v2.onrender.com/api/chat';

    // Toggle chat window
    function toggleChat() {
        isOpen = !isOpen;
        chatWindow.style.display = isOpen ? 'flex' : 'none';
        notificationBadge.style.display = 'none';
        
        if (isOpen) {
            chatInput.focus();
        }
    }

    // Add message to chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.style.marginBottom = '15px';
        messageDiv.style.display = 'flex';
        messageDiv.style.justifyContent = sender === 'user' ? 'flex-end' : 'flex-start';
        
        const bubbleDiv = document.createElement('div');
        bubbleDiv.style.maxWidth = '80%';
        bubbleDiv.style.padding = '10px 15px';
        bubbleDiv.style.borderRadius = '18px';
        bubbleDiv.style.fontSize = '14px';
        bubbleDiv.style.wordWrap = 'break-word';
        
        if (sender === 'user') {
            bubbleDiv.style.background = '#ff6b35';
            bubbleDiv.style.color = 'white';
            bubbleDiv.style.borderBottomRightRadius = '4px';
        } else {
            bubbleDiv.style.background = 'white';
            bubbleDiv.style.color = '#333';
            bubbleDiv.style.border = '1px solid #e9ecef';
            bubbleDiv.style.borderBottomLeftRadius = '4px';
        }
        
        bubbleDiv.textContent = text;
        messageDiv.appendChild(bubbleDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.style.marginBottom = '15px';
        typingDiv.style.display = 'flex';
        typingDiv.style.justifyContent = 'flex-start';
        
        const typingBubble = document.createElement('div');
        typingBubble.style.background = 'white';
        typingBubble.style.border = '1px solid #e9ecef';
        typingBubble.style.padding = '10px 15px';
        typingBubble.style.borderRadius = '18px';
        typingBubble.style.borderBottomLeftRadius = '4px';
        typingBubble.innerHTML = '<div style="display: flex; gap: 4px;"><div style="width: 8px; height: 8px; background: #ccc; border-radius: 50%; animation: typing 1.4s infinite ease-in-out;"></div><div style="width: 8px; height: 8px; background: #ccc; border-radius: 50%; animation: typing 1.4s infinite ease-in-out 0.2s;"></div><div style="width: 8px; height: 8px; background: #ccc; border-radius: 50%; animation: typing 1.4s infinite ease-in-out 0.4s;"></div></div>';
        
        typingDiv.appendChild(typingBubble);
        typingDiv.id = 'typing-indicator';
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Hide typing indicator
    function hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Send message to API
    async function sendMessage(text) {
        if (!text.trim()) return;

        // Add user message
        addMessage(text, 'user');

        // Show typing indicator
        showTypingIndicator();

        try {
            const response = await fetch(apiServerUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: text
                })
            });

            hideTypingIndicator();

            if (response.ok) {
                const data = await response.json();
                addMessage(data.response, 'bot');
            } else {
                addMessage("Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz", 'bot');
            }
        } catch (error) {
            hideTypingIndicator();
            addMessage("Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz", 'bot');
        }
    }

    // Event listeners
    chatToggle.addEventListener('click', toggleChat);
    chatClose.addEventListener('click', toggleChat);

    chatSend.addEventListener('click', () => {
        const message = chatInput.value.trim();
        if (message) {
            sendMessage(message);
            chatInput.value = '';
        }
    });

    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const message = chatInput.value.trim();
            if (message) {
                sendMessage(message);
                chatInput.value = '';
            }
        }
    });

    // Quick suggestion buttons
    document.querySelectorAll('.suggestion-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            sendMessage(btn.textContent);
        });
    });

    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes typing {
            0%, 60%, 100% { transform: translateY(0); }
            30% { transform: translateY(-10px); }
        }
        
        #chat-toggle:hover {
            transform: scale(1.1);
        }
        
        .suggestion-btn:hover {
            background: #f8f9fa !important;
            border-color: #ff6b35 !important;
        }
        
        #chat-send:hover {
            background: #e55a2b;
        }
    `;
    document.head.appendChild(style);

    // Show notification after 3 seconds if chat is not open
    setTimeout(() => {
        if (!isOpen) {
            notificationBadge.style.display = 'flex';
        }
    }, 3000);
})();
