import requests
import secret
import settings
import json
import pprint


class Parser:
    url = f"https://graph.facebook.com/v2.11/{settings.POST_ID}/{settings.DATA_TYPE}?access_token={secret.TOKEN}"
    data = dict()

    def main(self, log=True):
        while self.url is not None:
            if log:
                print(self.url)
            self.parse(json.loads(requests.get(self.url).content))

    def parse(self, response: dict):
        for datum in response["data"]:
            try:
                self.data[datum["type"]] += 1
            except KeyError:
                self.data[datum["type"]] = 1

        self.url = response["paging"].get("next")

    def __del__(self):
        pprint.pprint(self.data)


Parser().main()
