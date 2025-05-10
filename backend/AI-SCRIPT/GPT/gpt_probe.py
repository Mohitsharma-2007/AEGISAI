import requests

headers = {
    "User-Agent": "OpenAI-User-Agent-GPT-4",
    "X-Bot-Identifier": "gpt-4-sim"
}

response = requests.get("https://example.com/api/info", headers=headers)
print("GPT Probe Status:", response.status_code)
