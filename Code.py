pip install requests
import requests

ENDPOINT_URL = "https://api.openai.com/v1/chat/gpt3"
API_KEY = "YOUR_API_KEY_HERE"

#Sending Messages
def send_message(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "prompt": message,
        "temperature": 0.7,
        "max_tokens": 50,
        "stop": ["\n", "User:"]
    }

    response = requests.post(ENDPOINT_URL, headers=headers, json=data)
    return response.json()["choices"][0]["text"].strip()


response = send_message("Hello, how are you?")
print(response)

