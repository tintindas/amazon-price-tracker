import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.amazon.in/HONOR-Band-5-Meteorite-Black/dp/B07WTHFBQS/ref=sr_1_1?crid=2X4YEFGJU195L&dchild=1&keywords=honor+band+5&qid=1610218382&sprefix=hono%2Caps%2C390&sr=8-1"


def getData(url):

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }

    res = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(res.content, "html.parser")

    price = soup.find("span", attrs={"id": "priceblock_ourprice"}).text
    product_title = soup.find(id="productTitle").text.strip()
    time_stamp = datetime.now()

    data = {"product_name": product_title, "price": price, "time_stamp": time_stamp}

    return data


print(getData(url))
