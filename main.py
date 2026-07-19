from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.gq-magazine.co.uk/article/best-video-games-all-time")
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
games = soup.select('h2')

game_titles = []

for game in games:

    title = game.get_text(strip=True)

    if title and title[0].isdigit():
        game_titles.append(title)

game_titles = game_titles[::-1]

with open('games.txt', mode='w', encoding='utf-8') as file:
    file.write('\n'.join(game_titles))

print(f'{len(game_titles)} games saved to games.txt.')