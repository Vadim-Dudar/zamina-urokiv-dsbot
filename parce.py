import requests



class Parce():

    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'cookie': '__slsid=8564dd4b558496a7def4d18f57ce9d8f; path=/',
        }
        self.proxy = {
            'http': 'localhost:8080',
            'https': 'localhost:8080',
        }

    def html(self, url):
 
        with requests.session() as s:
            return s.post(url, headers=self.headers, proxies=self.proxy, cookies=s.cookies, verify=False)

            

    def parce(self):
        r = self.html(self.url)
        if r.status_code == 200:
            print('OK!')
        else:
            print(f'WRONG![{r.status_code}]')
            for el in r.cookies.items():
                print(el)

parce = Parce('https://goroskop.i.ua/').parce()