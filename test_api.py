import requests
import json

# Test the API directly
def test_api():
    url = "https://safari-chatbot-v2.onrender.com/api/chat"
    
    # Test data
    data = {
        "message": "Hello, what safaris do you offer?"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("Testing API...")
        print(f"URL: {url}")
        print(f"Data: {data}")
        
        response = requests.post(url, headers=headers, json=data)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Response: {result}")
        else:
            print(f"Error! Response text: {response.text}")
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_api()
