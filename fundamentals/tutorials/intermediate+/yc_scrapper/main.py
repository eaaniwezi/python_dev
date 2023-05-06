import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
response.raise_for_status()

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_text = []
article_link = []

articles = soup.find_all(name="span", class_="titleline")
for article_tag in articles:

    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.a.get("href")
    article_link.append(link)

article_points = [int(score.getText().split()[0])
                  for score in soup.find_all(name="span", class_="score")]


def get_highest_votes():
    index = article_points.index(max(article_points))

    highest_voted_article = article_text[index]
    highest_voted_article_votes = article_points[index]
    highest_voted_article_link = article_link[index]

    return {
        "highest_voted_article": highest_voted_article,
        "highest_voted_article_votes": highest_voted_article_votes,
        "highest_voted_article_link": highest_voted_article_link
    }

result = get_highest_votes()
print(result)