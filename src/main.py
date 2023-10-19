# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests as req

ARCHIVE_BASE_URL = "https://api.nytimes.com/svc/archive/v1/"
SEARCH_BASE_URL = "https://api.nytimes.com/svc/search/v2/"
API_KEY = "dzD9jUHnTM8t8i2ymFLS1RaEBkGsRYxs"

def get_params(section = "business", sort = "newest"):
    params = dict()
    params["api-key"] = API_KEY
    params["section"] = section
    params["sort"] = sort
    return params

def fetch_data(section, page):
    url = SEARCH_BASE_URL + "articlesearch.json"
    params = get_params(section=section)
    params["page"] = str(page)
    return req.get(url, params=params).json()

def process_data(responses):
    processed_data = dict()
    for response in responses:
        processed_data = dict()
        processed_data["abstract"] = response["abstract"]
        processed_data["url"] = response["web_url"]
        processed_data["body"] = response["lead_paragraph"]
        processed_data["abstract"] = response["abstract"]
        processed_data["abstract"] = response["abstract"]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    section = "business"
    data = fetch_data(section, 1)
    processed_data = process_data(data["response"]["docs"])
