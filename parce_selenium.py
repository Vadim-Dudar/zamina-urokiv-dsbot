from selenium import webdriver
from config import url, main_url

PROXY = "localhost:8080"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

with webdriver.Chrome() as driver:
    webdriver.ChromeOptions().add_argument('javascript.enabled')
    driver.get('http://hopes.epizy.com/')

