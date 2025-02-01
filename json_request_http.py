import requests

url = "https://sanket-make-render.onrender.com"
data = {
    "title": "Hello World",
    "body": "This is a test post",
    "userId": 1
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
