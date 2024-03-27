import requests

taken_url = 'http://127.0.0.1:8000/api-token-auth/'

credentials = {
    'username': 'FredR10',
    'password': 'Chivas4life',
}

response = requests.post(taken_url,data = credentials)
print(response.json())