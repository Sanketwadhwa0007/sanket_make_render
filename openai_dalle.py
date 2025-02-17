from openai import OpenAI
client = OpenAI()
client.api_key = "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"

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)