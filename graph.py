import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plotGraph(id):
    data = pd.read_csv(f"./data/{id}.csv")

    x = data["time_stamp"]
    y = data["price"]

    plt.plot(x, y)
    plt.savefig(f"./graphs/{id}.png")


plotGraph(1)