curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer xai-vjZoEHK70EIHbwFLWVyGCTpLTU4MemFc255g3JU0P0yAgQOJaZ34RMlr1ThKpCEZyGuwvTXXz3gGEC8l" -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and hello world and nothing else."
    }
  ],
  "model": "grok-2-latest",
  "stream": false,
  "temperature": 0
}'