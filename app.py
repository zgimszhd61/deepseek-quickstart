# python3
from openai import OpenAI

client = OpenAI(api_key="sk-", base_url="https://api.deepseek.com/")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ]
)

print(response.choices[0].message.content)
