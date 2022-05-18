import requests


class Super_Heroes:

    TOKEN = "2619421814940190"
    URL = f"https://superheroapi.com/api/{TOKEN}"

    def __init__(self, name: str):
        self.name = name
        URL = f"{Super_Heroes.URL}/search/{self.name}"
        self.__req = requests.get(URL).json()
        self._id = self.__req["results"][0]["id"]

    def get_intelligence(self):
        self.__url_in = f"{Super_Heroes.URL}/{self._id}/powerstats"
        self.__req_in = requests.get(self.__url_in).json()
        self.intelligence = int(self.__req_in['intelligence'])
        return int(self.intelligence)
