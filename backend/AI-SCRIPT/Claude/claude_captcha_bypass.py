import requests

data = {
    "username": "claude_ai",
    "password": "password123",
    "captcha": "bypass_attempt"
}

r = requests.post("https://example.com/login", data=data)
print("Claude CAPTCHA Bypass Attempt:", r.status_code)
