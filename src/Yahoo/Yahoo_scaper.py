import re
import csv
from time import sleep
from bs4 import BeautifulSoup
import requests

template = 'https://news.search.yahoo.com/search?p={}'
url = template.format("brexit")

headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'referer': 'https://www.google.com',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.findAll("div", "NewsArticle")
print(cards)

for card in cards:
    # find headline of the news article
    headline = card.find('h4', 's-title').text
    print(headline)
    #getting description
    description = card.find('p', 's-desc').text.strip()
    print(description)

