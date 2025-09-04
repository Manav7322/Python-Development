import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
headers = {"User-Agent": "Mozilla/5.0"}  # mimic a real browser
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Find the article title
title_tag = soup.find("h1", id="firstHeading")
if title_tag:
    print("Title:", title_tag.text)
else:
    print("Title not found")

# First 3 paragraphs
paragraphs = soup.select("div.mw-parser-output > p")
for p in paragraphs[:3]:
    print(p.get_text().strip())
