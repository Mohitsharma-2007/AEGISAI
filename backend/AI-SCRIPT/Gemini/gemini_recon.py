import requests
from bs4 import BeautifulSoup

urls = ["https://example.com", "https://example.com/about", "https://example.com/contact"]

for url in urls:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(f"Gemini crawled: {url} - Title: {soup.title.string if soup.title else 'N/A'}")
