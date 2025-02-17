# # Please install OpenAI SDK first: `pip3 install openai`

# from openai import OpenAI

# client = OpenAI(api_key="sk-b146e306cfe7455ca3d56f19d9da9ecb", base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)
import requests
from bs4 import BeautifulSoup

# Search Query
query = "sunset beach"
search_url = f"https://www.google.com/search?tbm=isch&q={query.replace(' ', '+')}"

# Set Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fetch the Google Image search results page
response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(response.content)
# Extract first image URL
image_tag = soup.find("img")
if image_tag and "src" in image_tag.attrs:
    image_url = image_tag["src"]

    # Download the image
    img_data = requests.get(image_url).content
    with open("first_image.jpg", "wb") as img_file:
        img_file.write(img_data)

    print("Image downloaded successfully as 'first_image.jpg'")
else:
    print("No image found!")
