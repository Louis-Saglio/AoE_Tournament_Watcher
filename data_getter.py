import json
import pprint

import requests
import time

import secret
import settings


class Parser:

    def __init__(self):
        self.url = f"https://graph.facebook.com/v2.11/{settings.POST_ID}/{settings.DATA_TYPE}?access_token={secret.TOKEN}"
        self.data = dict()
        self.log = {"url": False, "end": True}

    def main(self):
        while self.url is not None:
            if self.log["url"]:
                print(self.url)
            self.parse(json.loads(requests.get(self.url).content))
        return self.data

    def parse(self, response: dict):
        for datum in response["data"]:
            try:
                self.data[datum["type"]] += 1
            except KeyError:
                self.data[datum["type"]] = 1

        self.url = response["paging"].get("next")

    def __del__(self):
        if self.log["end"]:
            pprint.pprint(self.data)


while True:
    time.sleep(5)
    data = Parser().main()
    teutons = data["HAHA"]
    britons = data["LOVE"]
    with open("data", "a") as f:
        f.write(f"{teutons},{britons}\n")
