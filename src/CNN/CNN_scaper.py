from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

import time


# chrome = webdriver.Chrome()
#
# BASE_URL ="https://www.cnn.com/"
#
#
# def get_url_based_on_query(query="politics"):
#     page = 1
#
#     while True:
#         page_url = "?page=" + str(page)
#         params = "&size=50&from=0&sort=newest"
#         url = BASE_URL + query +  page_url +  params
#         try:
#             chrome.get(url)
#             time.sleep(10)
#
#             output_file = "CNN/"+ query + "_href.txt"
#             main_news_container = chrome.find_element(By.CLASS_NAME, 'stack')
#             text_sections = main_news_container.find_elements(By.CSS_SELECTOR, "a[href]")
#
#             with open(output_file, "a") as file:
#                 for elem in text_sections:
#                     # taking the news from 2020 to present
#                     link = elem.get_attribute("href")
#                     if link == "https://www.cnn.com/":
#                         continue
#                     is_valid = any(year in link for year in ["/2020/", "/2021/", "/2022/", "/2023/"])
#
#                     if is_valid:
#                         file.write(str(link))
#                         file.write("\n")
#                     else:
#                         break
#             page += 1
#         except:
#             break


def beautifulsoup():
    template = 'https://www.cnn.com/{}'
    url = template.format("politics")

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://www.google.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    section = soup.find("div", "zone--t-light")
    cards = section.findAll("div", "stack")
    print(cards)

    for card in cards:
        # find headline of the news article
        link = card.find('a', 'container_lead-plus-headlines__link').text
        print(link)



if __name__ == '__main__':
    beautifulsoup()


