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

def fetch_data(topic, page):
    url = SEARCH_BASE_URL + "articlesearch.json"
    params = get_params(section=topic)
    params["page"] = str(page)
    return req.get(url, params=params).json()