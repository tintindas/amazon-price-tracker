# import required libraries
import os
import smtplib
from email.message import EmailMessage
import requests


def send_email(data):

    level = "below" if data.price < data.target_price else "to"

    # Message to send if HTML is disabled
    message_body = f"""\
        The item you've been tracking has dropped {level} your target_price.

        {data.product_title} is now selling at {data.price}. 

        Product link: {data.url} 
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
            {data.product_title} is now selling at {data.price}. 
        </p>

        <a href="{data.url}">Product link</a>    
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
