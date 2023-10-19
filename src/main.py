# This is a sample Python script.
import json
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests as req

ARCHIVE_BASE_URL = "https://api.nytimes.com/svc/archive/v1/"
SEARCH_BASE_URL = "https://api.nytimes.com/svc/search/v2/"
API_KEY = "dzD9jUHnTM8t8i2ymFLS1RaEBkGsRYxs"

def get_params( sort = "newest"):
    params = dict()
    params["api-key"] = API_KEY
    params["sort"] = sort
    return params

def fetch_data_article_search(section, page):
    url = SEARCH_BASE_URL + "articlesearch.json"
    params = get_params()
    params["page"] = str(page)
    return req.get(url, params=params).json()

def fetch_data_archive(year, month):
    url = ARCHIVE_BASE_URL + str(year) + "/" + str(month) + ".json"
    params = get_params()
    return req.get(url, params=params).json()

def process_data(responses):
    processed_list = list()
    for response in responses:
        try:
            processed_data = dict()
            processed_data["abstract"] = str(response["abstract"])
            processed_data["url"] = str(response["web_url"])
            processed_data["body"] = str(response["lead_paragraph"])
            processed_data["published_on"] = str(response["pub_date"])
            processed_data["title"] = str(response["headline"]["main"])
            # processed_data["sub_section"] = str(response["subsection_name"])
            processed_data["section"] = str(response["section_name"])
            processed_list.append(processed_data)
        except :
            print("An error occured for response: ", response)
    return processed_list


def save_data(processed_data):
    output_file = "nytimes.jsonl"
    with open(output_file, 'a') as file:
        for data in processed_data:
            file.write(json.dumps(data))
            file.write("\n")

def fetch_and_save_yearly_data( year):
    # data = fetch_data_archive(year, 5)
    # time.sleep(2)
    # processed_data = process_data(data["response"]["docs"])
    # save_data(processed_data)
    for month in [11,12]:
        data = fetch_data_archive(year, month)
        time.sleep(5)
        try:
            processed_data = process_data(data["response"]["docs"])
            save_data(processed_data)
        except:
            print("An error occurred while processing data of year " + str(year) + " and month " + str(month))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fetch_and_save_yearly_data(2023)
    years = [2020, 2021, 2022, 2023]
    # years = [2022, 2023]
    # for year in years:
    #     fetch_and_save_yearly_data(year)


