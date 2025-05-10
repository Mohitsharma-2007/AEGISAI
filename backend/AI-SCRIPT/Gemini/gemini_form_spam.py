import requests

for i in range(5):
    res = requests.post("https://example.com/feedback", data={
        "name": "GeminiBot",
        "message": "Auto-generated feedback by Gemini AI LLM.",
    })
    print(f"Feedback {i+1} sent. Status:", res.status_code)
