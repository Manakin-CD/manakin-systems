import requests

url = 'https://magicloops.dev/api/loop/run/bc433371-1eed-4be9-9a07-35e44fb727be'
payload = {"request": "generate mock user data"}

response = requests.get(url, json=payload, verify=False)
responseJson = response.json()

print(f"STATUS: {responseJson['status']}")
print(f"OUTPUT: {responseJson['loopOutput']}")
print(f"Hola Tono")
