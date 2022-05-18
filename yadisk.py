from fake_useragent import UserAgent
import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.host = "https://cloud-api.yandex.net"
        self.headers = {"User-Agent": UserAgent().random,
                        "Content-Type": "application/json",
                        "Authorization": f"OAuth {self.token}"
                        }

    def __get_link(self, path):
        url = f"{self.host}/v1/disk/resources/upload/"
        headers = self.headers
        params = {"path": path, "overwrite": True}
        response = requests.get(url, params=params, headers=headers)
        return response.json()["href"]

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_link = self.__get_link(os.path.basename(file_path))
        response = requests.put(upload_link, data=open(
                file_path, "rb"), headers=self.headers)
        if response.status_code == 201:
            print("Completed")
