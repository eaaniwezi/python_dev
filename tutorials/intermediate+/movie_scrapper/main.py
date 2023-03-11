import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
response.raise_for_status()
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")


movie_data = soup.find_all(name="h3", class_="title")
all_movies = []

for movie in movie_data:
    all_movies.append(movie.getText())
print(all_movies[::-1])

with open("movies.txt", "w",encoding="utf-8") as file:
    for movie in all_movies[::-1]:
        file.write(movie)
        file.write("\n")
