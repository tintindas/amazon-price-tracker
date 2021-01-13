from data_handlers import appendData
from email_handler import send_email
from graph import plotGraph
from config import config
from scrape import getData

for item in config:
    data = getData(item)
    appendData(data)
    if data["price_num"] < data["target_price"]:
        send_email(data)
    else:
        print("Product is not below target price")
