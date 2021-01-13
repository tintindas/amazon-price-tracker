import requests
from bs4 import BeautifulSoup
from datetime import datetime


def getData(item):

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/75.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }

    res = requests.get(item["url"], headers=HEADERS)

    soup = BeautifulSoup(res.content, "html.parser")

    price = soup.find("span", attrs={"id": "priceblock_ourprice"}).text
    price_array = price.split("\xa0")
    price = " ".join(price_array)
    price_num = float(price_array[1].replace(",", ""))

    product_title = soup.find(id="productTitle").text.strip()
    time_stamp = datetime.now()

    data = {
        "id": item["id"],
        "product_name": product_title,
        "price": price,
        "price_num": price_num,
        "time_stamp": time_stamp,
        "url": item["url"],
        "target_price": item["target_price"],
    }

    return data