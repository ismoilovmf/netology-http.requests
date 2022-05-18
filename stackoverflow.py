from fake_useragent import UserAgent
from pprint import pprint
import requests
import datetime


class Stack_over:

    def __init__(self):
        self.host = "https://api.stackexchange.com/"
        self.headers = {"User-Agent": UserAgent().random,
                        "Content-Type": "application/json",
                        }
        self.date = str(datetime.date.today())
        self.date_old = f"{self.date[:8]}{int(self.date[8:])-2}"
        # print(self.date_old)
        # print(self.date)

    def get_tags(self, tag="Python"):
        self.url = self.host + "/2.3/questions?order=desc&sort=activity&site=stackoverflow"
        self.params = {
            "order": "desc",
            "sort": "activity",
            #"page": 10,
            #"pagesize": 2,
            "fromdate": self.date_old,
            "todate": self.date,
            "tagged": tag
        }
        response = requests.get(
            self.url, params=self.params, headers=self.headers).json()["items"]
        for resp in response:
            print(resp["title"], resp["link"], sep="\n")
            print()
            # pprint(response)
