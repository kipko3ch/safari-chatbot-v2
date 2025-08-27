// Safari Chat Widget Embed Script
(function() {
    // Create and inject the chat widget HTML
    const chatWidgetHTML = `
        <div id="safari-chat-widget" style="position: fixed; bottom: 20px; right: 20px; z-index: 10000; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <!-- Chat Toggle Button -->
            <div id="chat-toggle" style="width: 70px; height: 70px; background: linear-gradient(135deg, #8B4513, #D2691E, #FF8C00); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 6px 20px rgba(139, 69, 19, 0.3); transition: all 0.3s; border: 3px solid #FFF; position: relative; animation: pulse 2s infinite;">
                <div style="position: absolute; top: -5px; right: -5px; width: 20px; height: 20px; background: #FFD700; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #8B4513; font-weight: bold; animation: bounce 1s infinite;">💬</div>
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
            </div>

            <!-- Chat Window -->
            <div id="chat-window" style="position: absolute; bottom: 90px; right: 0; width: 380px; height: 550px; background: linear-gradient(135deg, #FFF8DC, #F5F5DC); border-radius: 20px; box-shadow: 0 12px 40px rgba(139, 69, 19, 0.2); display: none; flex-direction: column; overflow: hidden; border: 2px solid #D2691E;">
                <!-- Chat Header -->
                <div style="background: linear-gradient(135deg, #8B4513, #D2691E, #CD853F); color: white; padding: 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #FFD700;">
                    <div>
                        <div style="font-weight: bold; font-size: 18px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">🦁 Safari Expert</div>
                        <div style="font-size: 13px; opacity: 0.95; margin-top: 2px;">Nature Warriors African Safaris</div>
                    </div>
                    <div id="chat-close" style="cursor: pointer; font-size: 24px; background: rgba(255,255,255,0.2); border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; transition: all 0.2s;">×</div>
                </div>

                <!-- Chat Messages -->
                <div id="chat-messages" style="flex: 1; padding: 20px; overflow-y: auto; background: linear-gradient(135deg, #FFF8DC, #F5F5DC);">
                    <!-- Welcome message -->
                    <div style="margin-bottom: 20px;">
                        <div style="background: linear-gradient(135deg, #FFE4B5, #F0E68C); padding: 20px; border-radius: 15px; font-size: 15px; border: 2px solid #D2691E; box-shadow: 0 4px 15px rgba(139, 69, 19, 0.1);">
                            <div style="font-weight: bold; margin-bottom: 10px; color: #8B4513; font-size: 16px;">🌟 How can we help you today?</div>
                            <div style="color: #654321; line-height: 1.5;">Hi there! I'm your personal safari expert, ready to help you plan the adventure of a lifetime in Tanzania! Whether you're dreaming of the Serengeti, Kilimanjaro, or Zanzibar, I'm here to guide you every step of the way. What's calling your name today?</div>
                        </div>
                    </div>
                </div>

                <!-- Quick Suggestions -->
                <div id="quick-suggestions" style="padding: 20px; background: linear-gradient(135deg, #F5F5DC, #DEB887); border-top: 2px solid #D2691E;">
                    <div style="font-size: 13px; color: #8B4513; margin-bottom: 12px; font-weight: bold;">💡 Popular questions:</div>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                        <button class="suggestion-btn" style="background: linear-gradient(135deg, #FFF8DC, #FFE4B5); border: 2px solid #D2691E; padding: 10px 15px; border-radius: 25px; font-size: 13px; cursor: pointer; transition: all 0.3s; color: #8B4513; font-weight: 500; box-shadow: 0 2px 8px rgba(139, 69, 19, 0.1);">🦁 Serengeti Safari</button>
                        <button class="suggestion-btn" style="background: linear-gradient(135deg, #FFF8DC, #FFE4B5); border: 2px solid #D2691E; padding: 10px 15px; border-radius: 25px; font-size: 13px; cursor: pointer; transition: all 0.3s; color: #8B4513; font-weight: 500; box-shadow: 0 2px 8px rgba(139, 69, 19, 0.1);">🏔️ Kilimanjaro Trek</button>
                        <button class="suggestion-btn" style="background: linear-gradient(135deg, #FFF8DC, #FFE4B5); border: 2px solid #D2691E; padding: 10px 15px; border-radius: 25px; font-size: 13px; cursor: pointer; transition: all 0.3s; color: #8B4513; font-weight: 500; box-shadow: 0 2px 8px rgba(139, 69, 19, 0.1);">🏝️ Zanzibar Beach</button>
                        <button class="suggestion-btn" style="background: linear-gradient(135deg, #FFF8DC, #FFE4B5); border: 2px solid #D2691E; padding: 10px 15px; border-radius: 25px; font-size: 13px; cursor: pointer; transition: all 0.3s; color: #8B4513; font-weight: 500; box-shadow: 0 2px 8px rgba(139, 69, 19, 0.1);">📞 Chat with us</button>
                    </div>
                </div>

                <!-- Chat Input -->
                <div style="padding: 20px; background: linear-gradient(135deg, #F5F5DC, #DEB887); border-top: 2px solid #D2691E;">
                    <div style="display: flex; gap: 12px;">
                        <input type="text" id="chat-input" placeholder="Ask me about your dream safari..." style="flex: 1; padding: 12px 15px; border: 2px solid #D2691E; border-radius: 25px; outline: none; font-size: 14px; background: #FFF8DC; color: #8B4513; font-family: inherit;">
                        <button id="chat-send" style="background: linear-gradient(135deg, #8B4513, #D2691E); color: white; border: none; padding: 12px 20px; border-radius: 25px; cursor: pointer; font-size: 14px; font-weight: bold; box-shadow: 0 4px 12px rgba(139, 69, 19, 0.3); transition: all 0.3s;">Send</button>
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
            bubbleDiv.style.background = 'linear-gradient(135deg, #8B4513, #D2691E)';
            bubbleDiv.style.color = 'white';
            bubbleDiv.style.borderBottomRightRadius = '4px';
            bubbleDiv.style.boxShadow = '0 2px 8px rgba(139, 69, 19, 0.2)';
        } else {
            bubbleDiv.style.background = 'linear-gradient(135deg, #FFE4B5, #F0E68C)';
            bubbleDiv.style.color = '#8B4513';
            bubbleDiv.style.border = '2px solid #D2691E';
            bubbleDiv.style.borderBottomLeftRadius = '4px';
            bubbleDiv.style.boxShadow = '0 2px 8px rgba(139, 69, 19, 0.1)';
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
        typingBubble.style.background = 'linear-gradient(135deg, #FFE4B5, #F0E68C)';
        typingBubble.style.border = '2px solid #D2691E';
        typingBubble.style.padding = '12px 18px';
        typingBubble.style.borderRadius = '18px';
        typingBubble.style.borderBottomLeftRadius = '4px';
        typingBubble.style.boxShadow = '0 2px 8px rgba(139, 69, 19, 0.1)';
        typingBubble.innerHTML = '<div style="display: flex; gap: 4px;"><div style="width: 8px; height: 8px; background: #8B4513; border-radius: 50%; animation: typing 1.4s infinite ease-in-out;"></div><div style="width: 8px; height: 8px; background: #8B4513; border-radius: 50%; animation: typing 1.4s infinite ease-in-out 0.2s;"></div><div style="width: 8px; height: 8px; background: #8B4513; border-radius: 50%; animation: typing 1.4s infinite ease-in-out 0.4s;"></div></div>';
        
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
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-5px); }
            60% { transform: translateY(-3px); }
        }
        
        #chat-toggle:hover {
            transform: scale(1.1) !important;
            box-shadow: 0 8px 25px rgba(139, 69, 19, 0.4) !important;
        }
        
        .suggestion-btn:hover {
            background: linear-gradient(135deg, #FFD700, #FFA500) !important;
            border-color: #FF8C00 !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(139, 69, 19, 0.2) !important;
        }
        
        #chat-send:hover {
            background: linear-gradient(135deg, #654321, #8B4513) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(139, 69, 19, 0.4) !important;
        }
        
        #chat-close:hover {
            background: rgba(255,255,255,0.3) !important;
            transform: scale(1.1);
        }
    `;
    document.head.appendChild(style);

    // Create audio element for ding sound
    const dingSound = new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBSuBzvLZiTYIG2m98OScTgwOUarm7blmGgU7k9n1unEiBC13yO/eizEIHWq+8+OWT');
    
    // Function to play ding sound
    function playDing() {
        dingSound.volume = 0.3;
        dingSound.play().catch(e => console.log('Audio play failed:', e));
    }
    
    // Show notification with ding sound after 3 seconds if chat is not open
    setTimeout(() => {
        if (!isOpen) {
            notificationBadge.style.display = 'flex';
            playDing();
        }
    }, 3000);
    
    // Play ding when chat is opened
    const originalToggleChat = toggleChat;
    toggleChat = function() {
        if (!isOpen) {
            playDing();
        }
        originalToggleChat();
    };
})();
