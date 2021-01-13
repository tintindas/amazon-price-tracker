# import required libraries
import os
import smtplib
from email.message import EmailMessage
import requests
import datetime

# for testing

# product = {
#     "id": 1,
#     "product_name": "HONOR Band 5 (MeteoriteBlack)- Waterproof Full Color AMOLED Touchscreen, SpO2 (Blood Oxygen), Music Control, Watch Faces Store, up to 14 Day Battery Life",
#     "price": "₹\xa02,199.00",
#     "time_stamp": datetime.datetime(2021, 1, 13, 11, 26, 20, 941470),
#     "price_num": 2199.0,
#     "url": "https://www.amazon.in/HONOR-Band-5-Meteorite-Black/dp/B07WTHFBQS/ref=sr_1_1?crid=2X4YEFGJU195L&dchild=1&keywords=honor+band+5&qid=1610218382&sprefix=hono%2Caps%2C390&sr=8-1",
#     "target_price": 2000,
# }


def send_email(data):

    level = "below" if data["price_num"] < data["target_price"] else "to"

    product_name = data["product_name"]
    price = data["price"]
    url = data["url"]

    # Message to send if HTML is disabled
    message_body = f"""\
        The item you've been tracking has dropped {level} your target_price.

        {product_name} is now selling at {price}. 

        Product link: {url} 
        """

    # HTML message
    html_message = f"""\
        <!DOCTYPE html>
    <html lang="en">
    <body style="width: 400px">
        <p style="font-family: sans-serif">
            The item you have been tracking has dropped {level} your target price.     
        </p>
        <p>
            {product_name} <br><br> 
            is now selling at 
            <span style="font-weight: bold">{price}</span>
            . 
        </p>

        <a href="{url}">Product link</a>    
    </body>
    </html>
        """

    # Google Auth secrets
    user = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASSWORD")

    # Email content
    msg = EmailMessage()

    msg["Subject"] = "💸"
    msg["From"] = user
    msg["To"] = [user]
    msg.set_content(message_body)
    msg.add_alternative(html_message, subtype="html")

    # Send Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, password)

        smtp.send_message(msg)
        print("Message sent successfully")