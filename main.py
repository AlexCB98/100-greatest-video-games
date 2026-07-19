from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.gq-magazine.co.uk/article/best-video-games-all-time")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

games = soup.select('h2')

print(len(games))

for game in games:
    print(game.get_text())