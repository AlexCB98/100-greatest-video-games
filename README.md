# 100 Greatest Video Games

A Python web scraping project that collects the 100 greatest video games of all time from a British GQ ranking.

The games are extracted, ordered from first to last place, and saved in a text file.

---

## Features

- Scrapes game titles from a web page
- Filters unrelated HTML headings
- Orders the ranking from 1 to 100
- Saves the results in `games.txt`

---

## What I practiced

- Sending HTTP requests
- Parsing HTML with Beautiful Soup
- Selecting HTML elements
- Working with lists and strings
- Writing data to text files

---

## Project structure

```
main.py
games.txt
README.md
```

---

## How to run

Install the required packages:

```bash
pip install requests beautifulsoup4
```

Run the project:

```bash
python main.py
```

---

## Technologies used

- Python
- Requests
- Beautiful Soup
- HTML

---

## Data source

The ranking is collected from [British GQ's 100 greatest video games of all time](https://www.gq-magazine.co.uk/article/best-video-games-all-time).

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.