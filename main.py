import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies_titles = soup.find_all(name="h3", class_="title")

"""
for i in all_movies_titles:
    title_tag = str(i)
    title_str = (title_tag.split(">"))[1].split("<")[0]
    print(title_str)

    with open("best_100_movies.txt", mode="a") as txt_file:
        txt_file.write(f"\n{title_str}")
"""

#(Más corto)

movie_titles = [movie.getText() for movie in all_movies_titles]
#print(movie_titles[::-1])

for movie in movie_titles[::-1]:
    with open("best_100_movies.txt", mode="a") as txt_file:
        txt_file.write(f"{movie}\n")
    print(movie)