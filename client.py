import requests


url = "http://127.0.0.1:8001/"
data ={"content": "text"}
response = requests.post(url, json=data)
# response = requests.get(url)


print(response.status_code)
print(response.json())
