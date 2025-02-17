# import requests
# import json

# # Replace with your actual Groq Cloud API key and endpoint
# API_KEY = "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"
# API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Replace with the actual Groq API endpoint

# def call_groq_api(prompt):
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
    
#     data = {
#         "prompt": prompt,  # Your input prompt or query
#         "max_tokens": 100,  # Adjust based on your needs
#         "temperature": 0.7,  # Adjust for creativity vs. determinism
#         "top_p": 1.0,  # Sampling parameter
#         "n": 1  # Number of responses to generate
#     }
#     print(json.dumps(data))
#     response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    
#     if response.status_code == 200:
#         result = response.json()
#         return result.get("choices", [{}])[0].get("text", "").strip()
#     else:
#         print(f"Error: {response.status_code} - {response.text}")
#         return None

# # Example usage
# if __name__ == "__main__":
#     prompt = "Explain the concept of quantum computing in simple terms."
#     response = call_groq_api(prompt)
#     if response:
#         print(f"Response: {response}")
#     else:
#         print("Failed to get a response from the API.")
        
        
        
# from groq import Groq

# client = Groq()
# completion = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "user",
#             "content": "hi, tell me some business quotes to post on Instagram\n"
#         },
#         {
#             "role": "assistant",
#             "content": "Here are some inspiring business quotes to post on Instagram:\n\n1. **\"Believe you can and you're halfway there.\"** - Theodore Roosevelt\n2. **\"Success is not final, failure is not fatal: It is the courage to continue that counts.\"** - Winston Churchill\n3. **\"Don't watch the clock; do what it does. Keep going.\"** - Sam Levenson\n4. **\"The best way to get started is to quit talking and begin doing.\"** - Walt Disney\n5. **\"I have not failed. I've just found 10,000 ways that won't work.\"** - Thomas Edison\n6. **\"You don't have to be great to start, but you have to start to be great.\"** - Zig Ziglar\n7. **\"Entrepreneurship is living a few years of your life like most people won't, so that you can spend the rest of your life like most people can't.\"** - Gary Vaynerchuk\n8. **\"Do something today that your future self will thank you for.\"** - Unknown\n9. **\"The biggest risk is not taking any risk...\"** - Mark Zuckerberg\n10. **\"Hustle until you no longer have to introduce yourself.\"** - Gary Vaynerchuk\n\nFeel free to pick your favorite and post it on Instagram with a relevant image or graphic!\n\nWould you like more quotes or any specific theme (e.g., motivation, productivity, leadership)?"
#         }
#     ],
#     temperature=1,
#     max_completion_tokens=1024,
#     top_p=1,
#     stream=True,
#     stop=None,
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
# # This code snippet is using the `groq` library to interact with a chat completion API. Here's a
# # breakdown of what the code is doing:
import os

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what's the trending top topic on instagram? Give me one response in just one word ",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)