import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

movies = []

# Each movie row is inside <li> inside <ul> with data-testid
movie_list = soup.select("li.ipc-metadata-list-summary-item")[:10]
for movie in movie_list:
    title = movie.select_one("h3").get_text()
    metadata = movie.select_one(".cli-title-metadata")
    year = metadata.find("span").get_text(strip=True) if metadata else "N/A"
    rating_tag = movie.select_one("span.ipc-rating-star")
    rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"
    movies.append({
        "title": title,
        "year": year,
        "rating": rating
    })

for m in movies:
    print(f"{m['title']} ({m['year']}) - Rating: {m['rating']}")