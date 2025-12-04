import requests

response = requests.get('http://localhost:5000/api/health')
print("Status Code:", response.status_code)
print("Response:", response.json())
