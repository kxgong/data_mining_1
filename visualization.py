import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = '../youtube_trending/'
csv_list = ['CAvideos.csv', 'DEvideos.csv', 'FRvideos.csv', 'GBvideos.csv', 'INvideos.csv', 'JPvideos.csv',
            'KRvideos.csv', 'MXvideos.csv', 'RUvideos.csv', 'USvideos.csv']

def PLOT1(column,data):
    hist = data[column].hist(bins=50)
    plt.show()

def PLOT2(column,data):
    print(len(data[column]))
    data[column].plot.box()
    plt.show()

if __name__ == "__main__":
    # filepath = root + csv_list[0]
    filepath = "../wine_review/winemag-data_first150k.csv"
    data = pd.read_csv(filepath, header=0)

    # PLOT1("points",data)
    # PLOT1("price",data)
    # PLOT2("points", data)
    # PLOT2("price", data)
    PLOT1("views",data)
    PLOT1("likes",data)
    PLOT2("views", data)
    PLOT2("likes", data)