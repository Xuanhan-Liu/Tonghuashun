import requests


class Downloader:
    def __init__(self, url=None):
        self.url = url
        self.headers = None

    def load_headers(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.52 Safari/537.36",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            # "Host": "www.bankofdl.com",
            "Upgrade-Insecure-Requests": "1",
            # "Referer": "http://www.bankofdl.com/home/pc/gywm/cggg/list_2.shtml",
            "DNT": "1",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "9XGpi94x0WYiS=5SLO8Yk4tTpXPTnNxnkXiq6Lbt3rdCMnLQTOgpY_KgO7_ICr6CMmhSTpJXvOXjb.fGg7w8vqwUPdtGSW1jJLkXq; bankofdl=!HIPzhUzzO4Lzn+LsXef1LMEviPaE/2H1afQyn5Uejy3RnanU9z5cGyr1Rt5B+8Tp5SU3pi6lT6SszEU=; 9XGpi94x0WYiT=5MsjX.C0_NzqxcAPi3Wd9SAf.UnZ9ECaYfxFpWM7aHTQH7SS5J4sHlER5XE.Qf56BfRbAee8C5I1wiTdy6G9sTXha1Sy3rXHNM0NOx2_rbQi4GwuC0NVSyyBmgwZwrG6gvdxBaK_NAy7NTdVBMOo69zLoRTTcg7QN6EKh1YbgIAGV3p8DBYLvAlNU6L50uREjQr8H0J5P6VMqR3UdDSzIeCTMLSJR6W5.t2PNCoZK2M9upMGbp6gI3DW8z9KdmEsAa"
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
        print(res)
        if decode:
            return {'code': res.status_code, 'content': res.content.decode("utf-8")}
        return {'code': res.status_code, 'content': res.content}
