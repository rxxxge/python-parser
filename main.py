import requests
from bs4 import BeautifulSoup
from time import sleep
import os

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


def download(url):
    if not os.path.isdir("img"):
        os.mkdir("img")
        
    resp = requests.get(url, stream = True)
    r = open("/Users/tanya/Documents/Monty_Python/scraping/img/" + url.split("/")[-1], "wb")

    for value in resp.iter_content(1024**2):
        r.write(value)
    r.close()

def get_url():
    for count in range(1, 8):
        print("PAGE {0}".format(count))

        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")

        for element in data:
            card_url = "https://scrapingclub.com" + element.find("a").get("href")
            yield card_url

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers = headers)
        sleep(0)

        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_ = "card mt-4 my-4")

        name = data.find("h3", class_ = "card-title").text
        price = data.find("h4").text
        desc = data.find("p", class_ = "card-text").text
        img_link = "https://scrapingclub.com" + data.find("img", class_ = "card-img-top img-fluid").get("src")
        download(img_link)

        yield name, price, desc, img_link
        


