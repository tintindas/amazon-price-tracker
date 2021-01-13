from os import path
import pandas as pd

# for testing

# product = {
#     "id": 1,
#     "product_name": "HONOR Band 5 (MeteoriteBlack)- Waterproof Full Color AMOLED Touchscreen, SpO2 (Blood Oxygen), Music Control, Watch Faces Store, up to 14 Day Battery Life",
#     "price": "₹\xa02,199.00",
#     "price_num": 2199.00,
#     "time_stamp": datetime.datetime(2021, 1, 13, 11, 26, 20, 941470),
#     "url": "https://www.amazon.in/HONOR-Band-5-Meteorite-Black/dp/B07WTHFBQS/ref=sr_1_1?crid=2X4YEFGJU195L&dchild=1&keywords=honor+band+5&qid=1610218382&sprefix=hono%2Caps%2C390&sr=8-1",
#     "target_price": 2000,
# }


def appendData(product):
    id = product["id"]
    file_path = f"./data/{id}.csv"
    data = pd.DataFrame(columns=["price", "time_stamp"])

    if path.exists(file_path):
        data = pd.read_csv(file_path, index_col=0)

    new_row = pd.Series([product["price_num"], product["time_stamp"]], index=data.columns)

    data = data.append(new_row, ignore_index=True)

    data.to_csv(file_path)