import json

from bs4 import BeautifulSoup
import requests

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
template = 'https://www.cnn.com/{}'
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


def handle_individual_page(link="2023/10/22/politics/house-republican-speaker-race-who-is-running/index.html", topic = "politics"):
    url = template.format(link)

    try:
        response = get_beautified_response(url)
        section = response.find("div", "layout__content-wrapper")
        title_element = section.find("h1", "headline__text")
        title = title_element.text.strip("\n")

        author_element = section.find("span", "byline__name")
        author = author_element.text.strip("\n") if author_element is not None else ""

        publish_on_element = section.find("div", "timestamp")
        published_on = publish_on_element.text.strip("\n") if publish_on_element is not None else ""

        body_element = section.find("div", "article__content-container")
        paragraphs = body_element.findAll("p", "inline-placeholder")

        abstract = paragraphs[0].text.strip("\n") if paragraphs[0] is not None else ""
        paragraphs.pop(0)

        body = ""
        for paragraph in paragraphs:
            body += paragraph.text.strip("\n") if paragraph is not None else "" + "\n"

        data = {
            "title": title,
            "author": author,
            "published_on": published_on,
            "abstract": abstract,
            "body": body,
            "url": url,
            "section": topic
        }
        return data
    except Exception as e:
        print("An error has occurred: ", e)


def get_beautified_response(url):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'lxml')

def extract_and_save_links(url, topic):

    soup = get_beautified_response(url)
    section = soup.find("div", "zone--t-light")
    subsection = section.find("div", "zone__items")
    if section is None or subsection is None:
        # the response is emtpy
        raise Exception("The response does not have any data.")
    card_classname = "stack"
    if topic in ["opinions"]:
        card_classname = "opinions"
    cards = subsection.findAll("div", card_classname)

    file_name = "CNN/"+topic+".jsonl"
    with open(file_name, "a") as file:
        for card in cards:
            # find headline of the news article
            # the class name for style is different
            classname = "container_lead-plus-headlines__link"
            if topic in ["style"]:
                classname = "container_lead-plus-headlines-with-images__link"
            if topic in ["travel"]:
                classname = "container_vertical-strip__link"
            if topic in ["opinions"]:
                classname = "container_lead-plus-headlines__light"

            links = card.findAll('a', classname)
            if len(links) > 2:
                links.pop(0)
            for link in links:
                link_url = link.get("href")
                link_url = link_url[1:]

                try:
                    data = handle_individual_page(link_url, topic)
                    print(data)

                    file.write(json.dumps(data))
                    file.write("\n")
                except Exception as e:
                    print(e)


def beautifulsoup(topic = "politics"):
    url = template.format(topic)
    extract_and_save_links(url, topic)

if __name__ == '__main__':

    topics = ["politics", "us", "health", "entertainment", "style", "sport", "travel", "opinions","business"]
    # topics = ["opinions"]
    while True:
        for topic in topics:
            beautifulsoup(topic)
        # get data every hour
        print("Waiting for 1 hour to avoid getting duplicate data.")
        time.sleep(3600 * 6)



