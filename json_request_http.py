import requests

API_KEY = "AIzaSyDBP7iBCcS04fxjKm8BozKn97T9pghBAFI"
CX = "9643bcdb387014f7e"
# QUERY = "metgala"

# url = f"https://www.googleapis.com/customsearch/v1?q={QUERY}&cx={CX}&searchType=image&key={API_KEY}"

# response = requests.get(url).json()
# # print(response)
# # Extract image URLs
# image_urls = [item["link"] for item in response.get("items", [])]

# for url in image_urls:
#     print(url)



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


# url = "https://sanket-make-render.onrender.com/data"
# response = requests.post(url)
# print(response.text)

QUERY = "metgala"

url = f"https://www.googleapis.com/customsearch/v1?q={QUERY}&cx={CX}&searchType=image&key={API_KEY}"

response = requests.get(url).json()
# print(response)
# Extract image URLs
image_urls = [item["link"] for item in response.get("items", [])]

for url in image_urls:
    print(url)