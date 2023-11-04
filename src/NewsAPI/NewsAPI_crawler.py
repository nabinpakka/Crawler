import json

import requests as req

API_KEY = "752ef7fc89ce4dbeadabfeeefe694d04"
BASE_URL = "https://newsapi.org/v2/everything?from=2023-10-04&size=100&apiKey=" + API_KEY

def fetch_data_from_params(params):
    url = BASE_URL + params
    try:
        response = req.get(url)
        if response.status_code ==200:
            return response
        else:
            raise Exception("An error occured with status code: ", str(response.status_code))
    except Exception as e:
        print("An exception has occurred: ", e)


def fetch_from_domain(domain, page):
    param = "&domains="+ domain + "&page=" + str(page)
    return fetch_data_from_params(params=param)

def fetch_from_category(category):
    param = "&category=" + category
    return fetch_data_from_params(params=param)

def process_section(url, domain):
    # the section of the news can be obtained from url after the main domain name.

    if domain == "wsj.com":
        updated_url = url.replace("https://www.wsj.com/", "")
        url_split = updated_url.split("/")
        return url_split[0]
    elif domain == "bbc.co.uk":
        updated_url = url.replace("https://www.bbc.co.uk/news", "")
        url_split = updated_url.split("/")
        return url_split[0]

def process_article(article, domain):
    author = article["author"]
    title = article["title"]
    url = article["url"]
    abstract = article["description"]
    published_on = article["publishedAt"]
    section = process_section(url, domain)
    body = article["content"]

    return {
        "author": author,
        "title": title,
        "url": url,
        "abstract": abstract,
        "published_on": published_on,
        "section": section,
        "body": body
    }


if __name__ == '__main__':
    domain = "businessinsider.com"
    file_name = "businessinsider.json"

    page = 1
    while True:
        response = fetch_from_domain(domain, page)
        if response is None:
            break

        # response = fetch_from_category("sports")
        articles = json.loads(response.content.decode("utf-8"))["articles"]
        with open(file_name, "a") as file:
            for article in articles:
                processed_article = process_article(article, domain)
                file.write(json.dumps(processed_article))
                file.write("\n")
        if len(articles) >= 100:
            page += 1
            print(page, end=" | ")
        else:
            break



