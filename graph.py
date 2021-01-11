import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def plotGraph(id):
    data = pd.read_csv(f"./data/{id}.csv", header=0, index_col=0, parse_dates=True)
    date_format = "%Y-%m-%d %H:%M:%S.%f"

    time_stamp = data["time_stamp"]
    dates = [datetime.strptime(i, date_format) for i in time_stamp]
    days = [i.day for i in dates]
    prices = data["price"]

    x_labels = [d.strftime("%d %b") for d in dates]

    plt.plot(days, prices)
    plt.xticks(days, x_labels, rotation=45)
    plt.savefig(f"./graphs/{id}.png")