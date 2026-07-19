from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.gq-magazine.co.uk/article/best-video-games-all-time")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
games = soup.select('h2')

game_titles = []

for game in games:
    game_titles.append(game.get_text())

print(game_titles)