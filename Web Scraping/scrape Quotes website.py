import requests
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.select("div.quote")
for quote in quotes[:5]:
    text = quote.find("span", class_= "text").get_text()
    author = quote.find("small", class_ = "author").get_text()
    tags = [tag.get_text() for tag in quote.select(".tags a")]

    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags:{', '.join(tags)}")
    print("-"*50)