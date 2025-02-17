import requests

API_KEY = "AIzaSyDBP7iBCcS04fxjKm8BozKn97T9pghBAFI"
CX = "9643bcdb387014f7e"
QUERY = "metgala"

url = f"https://www.googleapis.com/customsearch/v1?q={QUERY}&cx={CX}&searchType=image&key={API_KEY}"

response = requests.get(url).json()
# print(response)
# Extract image URLs
image_urls = [item["link"] for item in response.get("items", [])]

for url in image_urls:
    print(url)
