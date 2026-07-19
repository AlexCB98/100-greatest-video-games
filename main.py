from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.gq-magazine.co.uk/article/best-video-games-all-time")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
games = soup.select('h2')

game_titles = []

for game in games:

    title = game.get_text(strip=True)

    if title and title[0].isdigit():
        game_titles.append(title)

print(game_titles)