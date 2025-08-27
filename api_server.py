import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Create Flask app for API server
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Your API key (kept secure on server)
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Knowledge base
KNOWLEDGE_BASE = """
COMPANY: Nature Warriors African Safaris
LOCATION: Arusha, Tanzania

CONTACT INFORMATION:
- Phone: +255625691470 | +255622127770
- Email: info@naturewarriorsafricansafaris.co.tz
- Location: Arusha, Tanzania

ABOUT US:
Nature Warriors African Safaris is your trusted partner for authentic Tanzanian safaris and beach holidays. We create personalized travel experiences that connect you with Tanzania's wildlife, landscapes, and cultures.

MAIN DESTINATIONS & SERVICES:

1. SERENGETI NATIONAL PARK
- Great Migration Experience - Witness the world-famous wildebeest migration
- Best time: July-September for migration
- Wildlife: Wildebeest, zebras, lions, cheetahs, leopards

2. NGORONGORO CRATER
- Ngorongoro Crater Tour - Descend into the crater for full-day safari
- Wildlife: Lions, rhinos, elephants, flamingos, hippos

3. ZANZIBAR ISLAND - Spice Island Paradise
- Nungwi Beach Retreat - Pristine beaches
- Stone Town Heritage Tour - UNESCO World Heritage site
- Zanzibar Spice Tour - Discover exotic spices
- Dolphin Watching Tour - Swim with dolphins
- Sunset Dhow Cruise - Traditional dhow sailing

4. MOUNT KILIMANJARO - Africa's Highest Peak (5,895m)
Climbing Routes Available:
- Machame Route "Whiskey Route" - Most popular, scenic
- Marangu Route "Coca-Cola Route" - Hut accommodation
- Lemosho Route - Premium, stunning views
- Rongai Route - Quieter, drier side

5. SELOUS GAME RESERVE
- Rufiji River Boat Safari - Unique boat safaris
- Selous Game Drive - Elephants, lions, wild dogs

BOOKING PROCESS:
1. Contact us via phone (+255625691470 or +255622127770) or email (info@naturewarriorsafricansafaris.co.tz)
2. Custom planning - We create personalized itinerary
3. Confirmation - Review and confirm with deposit
4. Adventure begins - Arrive in Tanzania for worry-free adventure

WHAT'S INCLUDED:
- Expert local guides
- Premium 4x4 safari vehicles
- Quality accommodations
- 24/7 support during trip
- All meals, park fees, transfers (package dependent)
"""

def get_groq_response(user_message):
    """Get response from Groq API"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # System prompt with comprehensive knowledge base
    system_message = {
        "role": "system",
        "content": f"""You are a friendly and professional assistant for Nature Warriors African Safaris, a Tanzania safari company. You help potential customers learn about our services and guide them to contact us for bookings and pricing.

{KNOWLEDGE_BASE}

CRITICAL INSTRUCTIONS:
1. NEVER mention specific prices - always direct people to contact us for pricing
2. Keep responses friendly, conversational, and concise (2-3 sentences max)
3. For any booking, pricing, or detailed information requests, provide our contact details
4. Focus on the experience and what makes us special, not technical details
5. Use a warm, welcoming tone that makes people excited about Tanzania
6. If someone asks about costs, say something like "For the best rates and personalized quotes, please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"
7. Always end with an encouraging note about contacting us to start their adventure

Remember: You're here to create excitement and guide people to contact us, not to provide all the details upfront."""
    }
    
    # Prepare messages with system prompt
    messages = [
        system_message,
        {"role": "user", "content": user_message}
    ]
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 400,
        "stream": False
    }
    
    try:
        print(f"Making request to Groq API...")
        print(f"URL: {url}")
        print(f"Headers: {headers}")
        print(f"Data: {data}")
        
        response = requests.post(url, headers=headers, json=data)
        print(f"Groq API Response Status: {response.status_code}")
        print(f"Groq API Response Headers: {dict(response.headers)}")
        
        if response.status_code != 200:
            print(f"Groq API Error Response: {response.text}")
            return f"Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"
        
        response_data = response.json()
        print(f"Groq API Success Response: {response_data}")
        
        return response_data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Groq API Request Exception: {e}")
        return f"Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"
    except Exception as e:
        print(f"Groq API General Exception: {e}")
        return f"Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chat requests"""
    try:
        print("=== Chat endpoint called ===")
        print(f"API Key available: {bool(GROQ_API_KEY)}")
        
        # Check if API key is available
        if not GROQ_API_KEY:
            print("ERROR: API key not configured")
            return jsonify({
                'error': 'API key not configured',
                'response': "Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"
            }), 500
        
        data = request.get_json()
        print(f"Received data: {data}")
        
        user_message = data.get('message', '')
        print(f"User message: {user_message}")
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from Groq API
        print("Calling Groq API...")
        response = get_groq_response(user_message)
        print(f"Groq response: {response}")
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': 'Internal server error',
            'response': "Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"
        }), 500

@app.route('/api/chat', methods=['GET'])
def chat_get():
    """Handle GET requests to chat endpoint"""
    return jsonify({
        'error': 'Method not allowed',
        'message': 'Use POST method to send chat messages'
    }), 405

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    api_key_status = "configured" if GROQ_API_KEY else "not configured"
    return jsonify({
        'status': 'healthy', 
        'message': 'API server is running',
        'api_key_status': api_key_status,
        'api_key_length': len(GROQ_API_KEY) if GROQ_API_KEY else 0
    })

@app.route('/embed-script.js', methods=['GET'])
def embed_script():
    """Serve the embed script"""
    script_content = '''// Safari Chat Widget Embed Script
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
                        <div style="background: linear-gradient(135deg, #FFE4B5, #F0E68C); padding: 20px; border-radius: 15px; font-size: 15px; border: 2px solid #D2691E; box-shadow: 0 4px 15px rgba(139, 69, 19, 0.1);">
                            <div style="font-weight: bold; margin-bottom: 10px; color: #8B4513; font-size: 16px;">🌟 How can we help you today?</div>
                            <div style="color: #654321; line-height: 1.5;">Hi there! I'm your personal safari expert, ready to help you plan the adventure of a lifetime in Tanzania! Whether you're dreaming of the Serengeti, Kilimanjaro, or Zanzibar, I'm here to guide you every step of the way. What's calling your name today?</div>
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
})();'''
    
    return script_content, 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    # Run the Flask app
    print("🚀 Starting API Server...")
    print("📡 API Server running on: http://localhost:5000")
    print("🔗 Chat endpoint: http://localhost:5000/api/chat")
    print("💚 Health check: http://localhost:5000/api/health")
    print("\n🔒 Your API key is now secure on the server!")
    print("🌐 You can now embed the chat widget on any website safely.")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
