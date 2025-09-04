import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

books = soup.select("ol.row li")

for book in books[:10]:
    title = book.h3.a["title"]
    price = book.find("p",class_ = "price_color").get_text()
    availability = book.find("p",class_="instock availability").get_text(strip= True)
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print("-" * 50)