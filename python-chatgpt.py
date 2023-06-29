import requests

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
API_KEY = "api_key_here"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write a python script for hello world",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(API_ENDPOINT, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {str(response.status_code)}")