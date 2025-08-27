import streamlit as st
import requests
import json
import os

# Page configuration for embedding
st.set_page_config(
    page_title="Nature Warriors Safari Assistant",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Hide Streamlit branding and menu for embedding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive design */
    .stApp {
        background-color: #f8f9fa;
        max-width: 100%;
    }
    
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        .stApp > div {
            padding: 0.5rem;
        }
        
        .chat-message {
            max-width: 95% !important;
            font-size: 14px;
        }
        
        .suggestion-button {
            font-size: 12px !important;
            padding: 0.3rem 0.6rem !important;
            margin: 0.2rem !important;
        }
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        align-self: flex-end;
        max-width: 80%;
        margin-left: auto;
    }
    
    .assistant-message {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        align-self: flex-start;
        max-width: 80%;
        color: #333;
    }
    
    .welcome-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .suggestion-button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        margin: 0.3rem;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.3s ease;
        display: inline-block;
        text-decoration: none;
    }
    
    .suggestion-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .help-text {
        background: rgba(255,255,255,0.9);
        padding: 0.8rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 4px solid #4facfe;
        font-size: 14px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

KNOWLEDGE_BASE = """
COMPANY: Nature Warriors African Safaris
LOCATION: Arusha, Tanzania

CONTACT INFORMATION:
- Phone: +255625691470 | +255622127770
- Email: info@naturewarriorsafricansafaris.co.tz
- Location: Arusha, Tanzania

ABOUT US:
Nature Warriors African Safaris is your trusted partner for authentic Tanzanian safaris and beach holidays. We create personalized travel experiences that connect you with Tanzania's wildlife, landscapes, and cultures. From wildlife safaris to cultural immersions, mountain climbs to beach escapes - we create extraordinary Tanzania experiences.

MAIN DESTINATIONS & SERVICES:

1. SERENGETI NATIONAL PARK
- Great Migration Experience (3 Days/2 Nights) - Witness the world-famous wildebeest migration and dramatic river crossings
- Best time: July-September for migration
- Wildlife: Wildebeest, zebras, lions, cheetahs, leopards

2. NGORONGORO CRATER
- Ngorongoro Crater Tour (1 Day) - Descend into the crater for full-day safari
- Wildlife: Lions, rhinos, elephants, flamingos, hippos
- Known as "Africa's Garden of Eden"

3. ZANZIBAR ISLAND - Spice Island Paradise
- Nungwi Beach Retreat (3 Days/2 Nights) - Pristine beaches with crystal-clear waters
- Stone Town Heritage Tour (Half Day) - UNESCO World Heritage site with Arabic, Indian, and African influences
- Zanzibar Spice Tour (Half Day) - Discover exotic spices and agricultural heritage
- Dolphin Watching Tour (Half Day) - Swim with dolphins and snorkeling
- Jozani Forest Tour (2 Hours) - Meet rare red colobus monkeys
- Sunset Dhow Cruise (2 Hours) - Traditional dhow sailing at sunset

4. MOUNT KILIMANJARO - Africa's Highest Peak (5,895m)
Climbing Routes Available:
- Machame Route "Whiskey Route" (6-7 days) - Most popular, scenic, camping
- Marangu Route "Coca-Cola Route" (5-6 days) - Cheapest, hut accommodation
- Lemosho Route (7-8 days) - Premium, stunning views, high success rate
- Rongai Route (6-7 days) - Quieter, drier side
- Northern Circuit Route (8-9 days) - Longest, highest success rate
- Shira Route (6-8 days) - Challenging, scenic
- Umbwe Route (5-6 days) - Steepest, most difficult

5. SELOUS GAME RESERVE - Africa's Largest Game Reserve
- Rufiji River Boat Safari (Half Day) - Unique boat safaris spotting hippos, crocodiles, birdlife
- Selous Game Drive (1 Day) - Elephants, lions, wild dogs in vast wilderness
- Walking Safari (2 Hours) - Bush walks with expert guides

6. MIKUMI NATIONAL PARK
- Mikumi Game Drive (1 Day) - Elephants, lions, giraffes in open plains
- Hippo Pool Visit (Half Day) - Observe hippos up close
- Mikumi Birdwatching (2 Hours) - Rich birdlife tours

7. RUAHA NATIONAL PARK
- Ruaha Game Drive (1 Day) - Lions, elephants, kudu in vast wilderness
- Known for baobab trees and African wild dogs

8. ARUSHA
- Gateway to northern Tanzania parks
- Mount Meru trekking available

SPECIALIZED EXPERIENCES:
- Honeymoon Packages - Romantic safari and beach combinations
- Group Tours - Special rates for families and corporate retreats
- Educational Tours - Learning-focused for students and researchers
- Flying Safaris - Time-efficient using small aircraft
- Accessible Safaris - Modified for travelers with mobility challenges
- Luxury Experiences - Ultra-premium with helicopter transfers
- Photography Safaris - Specialized for wildlife photography

BOOKING PROCESS:
1. Contact us via phone (+255625691470 or +255622127770) or email (info@naturewarriorsafricansafaris.co.tz)
2. Custom planning - We create personalized itinerary based on your interests
3. Confirmation - Review itinerary and confirm with secure deposit
4. Adventure begins - Arrive in Tanzania for worry-free adventure

WHAT'S INCLUDED:
- Expert local guides with extensive wildlife and cultural knowledge
- Premium 4x4 safari vehicles with pop-up roofs and charging ports
- Quality accommodations from budget-friendly to luxury
- 24/7 support during your trip
- All meals, park fees, and airport transfers (package dependent)

BEST TIME TO VISIT:
- Dry season (June-October): Best wildlife viewing
- Great Migration: July-September in Serengeti
- Green season (November-May): Lush landscapes, bird watching

KILIMANJARO CLIMBING DETAILS:
- Expert certified mountain guides with wilderness first aid training
- Daily health checks and oxygen monitoring
- High-quality camping gear and nutritious meals
- Fair wages paid to porters and guides
- Emergency evacuation procedures in place

ZANZIBAR HIGHLIGHTS:
- Powder-white beaches and turquoise lagoons
- Stone Town's narrow alleys with ornate doorways and bustling bazaars
- Spice tours showing why it's called the "Spice Island"
- Marine activities: snorkeling, diving, dolphin watching
- Cultural blend of Arabian, Indian, and African influences

CONTACT FOR BOOKING:
Phone: +255625691470 | +255622127770
Email: info@naturewarriorsafricansafaris.co.tz
Location: Arusha, Tanzania
"""

QUESTION_SUGGESTIONS = [
    "What safari packages do you offer?",
    "How do I book a Kilimanjaro trek?",
    "What's included in your safari packages?",
    "Best time to visit Serengeti?",
    "Zanzibar beach holiday options?",
    "What are your contact details?",
    "Kilimanjaro climbing routes?",
    "Great Migration safari timing?"
]

def get_groq_response(messages, api_key):
    """Get response from Groq API"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
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
    full_messages = [system_message] + messages
    
    data = {
        "model": "llama-3.1-70b-versatile",
        "messages": full_messages,
        "temperature": 0.7,
        "max_tokens": 400
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Sorry, I'm having trouble connecting right now. Please contact us directly at +255625691470 or info@naturewarriorsafricansafaris.co.tz"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for API key (collapsible for embedding)
with st.sidebar:
    st.title("🦁 Safari Assistant")
    api_key = st.text_input(
        "Groq API Key", 
        type="password", 
        value=os.getenv("GROQ_API_KEY", ""),
        help="API key is pre-filled. You can modify if needed."
    )
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🦁 Nature Warriors Safari Assistant")

# Welcome message with non-obtrusive "How can we help you?"
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-message">
        <h3>🌍 How can we help you plan your Tanzania adventure?</h3>
        <p>Ask me about safaris, Kilimanjaro treks, Zanzibar beaches, or booking information!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**💡 Popular Questions:**")
    
    # Create columns for responsive button layout
    cols = st.columns(2)
    for i, suggestion in enumerate(QUESTION_SUGGESTIONS):
        col = cols[i % 2]
        if col.button(suggestion, key=f"suggestion_{i}", help="Click to ask this question"):
            if api_key:
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": suggestion})
                
                # Get assistant response
                response = get_groq_response(st.session_state.messages, api_key)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
            else:
                st.error("Please enter your Groq API key in the sidebar first.")

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask about safaris, destinations, Kilimanjaro treks, Zanzibar holidays, or booking..."):
    if not api_key:
        st.error("Please enter your Groq API key in the sidebar to start chatting.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_groq_response(st.session_state.messages, api_key)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("""
<div class="help-text">
<strong>📱 Responsive Design:</strong> This chatbot works perfectly on all devices - desktop, tablet, and mobile!<br>
<strong>🔗 To embed in your website:</strong> Use the iframe code below with your deployed Streamlit app URL.
</div>
""", unsafe_allow_html=True)

st.code("""
<iframe 
    src="YOUR_STREAMLIT_APP_URL" 
    width="100%" 
    height="600" 
    frameborder="0"
    style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</iframe>
""", language="html")
