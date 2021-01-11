from os import path
import pandas as pd
from datetime import datetime

now = datetime.now()
product = {"id": 1, "price": 2000, "time_stamp": now}


def appendData(product):
    id = product["id"]
    file_path = f"./data/{id}.csv"
    data = pd.DataFrame(columns=["price", "time_stamp"])

    if path.exists(file_path):
        data = pd.read_csv(file_path, index_col=0)

    print(data)

    new_row = pd.Series([product["price"], product["time_stamp"]], index=data.columns)

    data = data.append(new_row, ignore_index=True)

    data.to_csv(file_path)