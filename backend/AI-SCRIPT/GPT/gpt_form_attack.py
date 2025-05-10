import requests

for i in range(10):
    data = {
        "name": "GPTBot",
        "email": f"gptbot{i}@openai.fake",
        "message": "This is an LLM-generated message attempting to spam the contact form."
    }
    r = requests.post("https://example.com/contact", data=data)
    print(f"Attack {i+1} Status:", r.status_code)
