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
- Great Migration Experience (3 Days/2 Nights) - Witness the world-famous wildebeest migration
- Best time: July-September for migration
- Wildlife: Wildebeest, zebras, lions, cheetahs, leopards

2. NGORONGORO CRATER
- Ngorongoro Crater Tour (1 Day) - Descend into the crater for full-day safari
- Wildlife: Lions, rhinos, elephants, flamingos, hippos

3. ZANZIBAR ISLAND - Spice Island Paradise
- Nungwi Beach Retreat (3 Days/2 Nights) - Pristine beaches
- Stone Town Heritage Tour (Half Day) - UNESCO World Heritage site
- Zanzibar Spice Tour (Half Day) - Discover exotic spices
- Dolphin Watching Tour (Half Day) - Swim with dolphins
- Sunset Dhow Cruise (2 Hours) - Traditional dhow sailing

4. MOUNT KILIMANJARO - Africa's Highest Peak (5,895m)
Climbing Routes Available:
- Machame Route "Whiskey Route" (6-7 days) - Most popular, scenic
- Marangu Route "Coca-Cola Route" (5-6 days) - Cheapest, hut accommodation
- Lemosho Route (7-8 days) - Premium, stunning views
- Rongai Route (6-7 days) - Quieter, drier side

5. SELOUS GAME RESERVE
- Rufiji River Boat Safari (Half Day) - Unique boat safaris
- Selous Game Drive (1 Day) - Elephants, lions, wild dogs

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
        "content": f"""You are a helpful assistant for Nature Warriors African Safaris, a Tanzania safari company. Use the following comprehensive knowledge base to answer questions about the company, services, destinations, and booking information.

{KNOWLEDGE_BASE}

INSTRUCTIONS:
1. Always answer based on the knowledge base first
2. For booking questions, provide the exact contact information: +255625691470 | +255622127770 or info@naturewarriorsafricansafaris.co.tz
3. For service questions, mention specific packages, destinations, and durations
4. If the question is not covered in the knowledge base, provide a polite general response
5. Keep answers concise, clear, and professional (2-3 sentences max)
6. Always be helpful and encouraging about Tanzania safari experiences
7. Use specific details from the knowledge base like prices, durations, and what's included

If someone asks about booking, services, contact info, or destinations, use the exact information from the knowledge base above."""
    }
    
    # Prepare messages with system prompt
    messages = [
        system_message,
        {"role": "user", "content": user_message}
    ]
    
    data = {
        "model": "llama-3.1-70b-versatile",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 400
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chat requests"""
    try:
        # Check if API key is available
        if not GROQ_API_KEY:
            return jsonify({
                'error': 'API key not configured',
                'response': "Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"
            }), 500
        
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from Groq API
        response = get_groq_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
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
    return jsonify({'status': 'healthy', 'message': 'API server is running'})

if __name__ == '__main__':
    # Run the Flask app
    print("🚀 Starting API Server...")
    print("📡 API Server running on: http://localhost:5000")
    print("🔗 Chat endpoint: http://localhost:5000/api/chat")
    print("💚 Health check: http://localhost:5000/api/health")
    print("\n🔒 Your API key is now secure on the server!")
    print("🌐 You can now embed the chat widget on any website safely.")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
