import random
import requests


class Downloader:
    def __init__(self, url=None, file_path='./config/ua.txt'):
        self.url = url
        self.headers = None
        with open(file_path, 'r', encoding='utf-8') as file:
            self.UAs = file.read().split('\n')

    def load_headers(self):
        idx = random.randint(0, len(self.UAs))
        self.headers = {
            "User-Agent": self.UAs[idx],
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Upgrade-Insecure-Requests": "1",
            "DNT": "1",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
        }
        self.proxies = {
        }

    def load_url(self, url):
        self.url = url

    def download(self, decode=False):
        self.load_headers()
        res = requests.get(self.url, headers=self.headers, proxies=self.proxies)
        if decode:
            return {'code': res.status_code, 'content': res.content.decode("utf-8")}
        return {'code': res.status_code, 'content': res.content}

    def session(self, decode=False):
        self.load_headers()
        session = requests.Session()
        res = session.get(self.url, headers=self.headers)
        if decode:
            return {'code': res.status_code, 'content': res.content.decode("utf-8")}
        return {'code': res.status_code, 'content': res.content}
