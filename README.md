# amazon-price-tracker
Tracks price of given product on amazon and sends e-mail notification if the price drops below a given threshold.

## Set up

### Google Set up

1. Go to the following link to set up an app password for your google account.

      [Link](https://myaccount.google.com/apppasswords)

1. Set email address and password generated for third-party app as environment variables.
    ```
    export EMAIL_USER=<Your email id>
    export EMAIL_PASSWORD=<Generated password>
    ```
    

You may have to set up 2FA if you have not already.

### Repository Set up
1. Clone the repository

    `git clone https://github.com/tintindas/amazon-price-tracker.git`

1. Navigate into directory

    `cd amazon-price-tracker`

1. Set up Python virtual environment

    `python3 -m venv .venv`
  
    .venv is what I usually name my virtual environment folder. 

1. Activate environment
  
    `$ source .venv/bin/activate`

1. Install dependencies
  
    `$ pip install -r requirements.txt`

 1. Edit email list
 
    Edit the line below. Reset the array with your email addresses.
 
       [`msg['To'] = ['upamanyudas16@gmail.com']](https://github.com/tintindas/amazon-price-tracker/blob/5e9fb2cf8e7c6ed1dcc6f5a55f69f31500b3a69b/email_handler.py#L67)
       
### Config
1. Put the url(s) of your product(s) in the config array in the config.py. 
1. The `id` property of the object must be unique. 
1. Each product must be its own object with a target price, unique id and url.

### Workflow
Change the cron schedule to run the workflow in check_price.yml at your intended interval.

[`    - cron: "0 */8 * * *"`](https://github.com/tintindas/amazon-price-tracker/blob/5e9fb2cf8e7c6ed1dcc6f5a55f69f31500b3a69b/.github/workflows/check_price.yml#L11)
