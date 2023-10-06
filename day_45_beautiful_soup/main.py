import bs4
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
response.raise_for_status()
content = response.text

soup = bs4.BeautifulSoup(content, "html.parser")

all_movies = [item.getText() for item in soup.find_all(name="h3", class_="title")]
all_movies.reverse()

with open("output.txt", "w", encoding="utf-8") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")
        print(movie)

