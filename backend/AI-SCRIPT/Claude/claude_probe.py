import requests

headers = {
    "User-Agent": "Claude-Agent",
    "X-AI-Agent": "Claude-3-Test"
}

res = requests.get("https://example.com/api/check", headers=headers)
print("Claude Probe Status:", res.status_code)
