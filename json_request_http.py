import requests

url = "https://sanket-make-render.onrender.com/data"
data = {
    "title": "Hello World",
    "body": "This is a test post",
    "userId": 1
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)


print(response.status_code)
print(response.json())


url = "https://sanket-make-render.onrender.com/auth/facebook/callback"
response = requests.post(url)
print(response)