import requests

url = "https://app.ayrshare.com/api/post"
headers = {
    "Authorization": "Bearer 820A6707-A62641AE-AA4AEAED-2AECC87F",
    "Content-Type": "application/json"
}
data = {
    "post": "Today is a great day!",
    "platforms": ["instagram"],
    "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"]
}

response = requests.post(url, json=data, headers=headers)
print(response.json())