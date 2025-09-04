import requests
from bs4 import BeautifulSoup

url="https://news.ycombinator.com/"

headers = {"User-Agent": "Mozilla/5.0"}  # mimic a real browser
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text,"html.parser")

headlines = soup.select_one("span.titleline a")
print("Headline:", headlines.get_text())
print("Link:", headlines["href"])

score = soup.select_one("span.score")
if score:
    print("Score:",score.get_text())
else:
    print("Score: Not found (maybe 0 points yet)")