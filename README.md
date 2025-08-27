# 🌍 Nature Warriors Safari Chat Widget

A secure, embeddable chat widget for Nature Warriors African Safaris with AI-powered responses.

## 🔒 Security Features

- **Secure API Server**: API key is protected on the server
- **No Frontend Exposure**: API key never appears in client-side code
- **CORS Enabled**: Works across different domains

## 🚀 Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the API server:**
   ```bash
   python api_server.py
   ```

3. **Test the chat widget:**
   - Open `chat-widget.html` in your browser
   - Ask questions about safaris, Kilimanjaro, or Zanzibar

### Production Deployment (Render)

1. **Upload to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/safari-chatbot.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Connect your GitHub repository
   - Create a new Web Service
   - Render will automatically detect the Python app
   - Deploy!

3. **Update chat widget URL:**
   - After deployment, update the API URL in `chat-widget.html`:
   ```javascript
   this.apiServerUrl = 'https://your-app-name.onrender.com/api/chat';
   ```

## 📁 Files

- `api_server.py` - Flask API server (keeps API key secure)
- `chat-widget.html` - Embeddable chat widget
- `app.py` - Streamlit version (alternative)
- `requirements.txt` - Python dependencies
- `render.yaml` - Render deployment config

## 🌐 Embedding

Add this to any website:

```html
<iframe 
    src="chat-widget.html" 
    style="position: fixed; bottom: 0; right: 0; z-index: 9999; width: 400px; height: 600px; border: none;"
    frameborder="0"
    title="Safari Chat Assistant"
></iframe>
```

## 🔧 API Endpoints

- `GET /api/health` - Health check
- `POST /api/chat` - Chat endpoint (send JSON with `message` field)

## 📞 Contact

Nature Warriors African Safaris:
- Phone: +255625691470 | +255622127770
- Email: info@naturewarriorsafricansafaris.co.tz
- Location: Arusha, Tanzania
