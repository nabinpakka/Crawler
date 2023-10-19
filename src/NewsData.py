import json

class NewsData:

    def __init__(self, id, headline, abstract, url, body, published_on):
        self.id = id
        self.headline = headline
        self.abstract = abstract
        self.url = url
        self.body = body
        self.published_on = published_on

    def to_json(self):
        data = {
            "id": self.id,
            "headline": self.headline,
            "abstract": self.abstract,
            "url": self.url,
            "body": self.body,
            "published_on": self.published_on
        }
        return json.dumps(data)
