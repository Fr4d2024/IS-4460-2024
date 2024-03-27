import requests

api_url = 'http://127.0.0.1:8000/api/customers'

token = "d1169ff9914bf1eed1608ee8c37298162ab4f24e"

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(api_url,headers=headers)

print(response.status_code)

if response.status_code == 200:
    print(f"Customer retrieval successful. {response.text}")
else:
    print(f"Customer retrieval failed. {response.text}")