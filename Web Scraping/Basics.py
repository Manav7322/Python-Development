import requests
from bs4 import BeautifulSoup

url="https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.select("span.titleline a")

for h in headlines[:5]:
    print(h.text, "->", h["href"])