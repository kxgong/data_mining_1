import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostRegressor
# root = '../youtube_trending/'
# csv_list = ['CAvideos.csv', 'DEvideos.csv', 'FRvideos.csv', 'GBvideos.csv', 'INvideos.csv', 'JPvideos.csv',
#             'KRvideos.csv', 'MXvideos.csv', 'RUvideos.csv', 'USvideos.csv']


def remove_missing(data):
    data_temp = data
    Data1 = data.dropna(axis=0)
    # data_temp.append(Data1, ignore_index=True)
    hist = Data1.hist(bins=100)
    print(data_temp)
    # print(len(Data1))
    # data_temp.append(Data1)
    plt.show()

def five_number(str2,data2):
    nums = data2[str2]
    nullnum = nums.isnull().sum()
    print(f'num: {nullnum}')
    nums = nums.dropna(axis=0)
    Min = min(nums)
    Max = max(nums)
    Q1 = np.percentile(nums, 25)
    Median = np.median(nums)
    Q3 = np.percentile(nums, 75)
    print(f'Min: {Min}, Q1: {Q1}, Median: {Median}, Q3: {Q3}, Max: {Max}')

def fill_most_frequent(data):
    Data2 = data.fillna(data.mode())
    # 绘制直方图
    hist2 = Data2.hist(bins=100)
    # # 绘制盒图
    # Data2.plot.box()
    plt.show()


def relation(data):
    hist = data['price'].hist(bins=20)
    five_number('price', data)
    known = []
    unknown = []
    known_pre = data[data.notnull()].values
    for i in known_pre:
        if i[1] != i[1]:
            unknown.append(i)
        else:
            known.append(i)
    # unknown = data[data.isnull()].values
    print(len(known))
    print(len(unknown))
    known = np.array(known)
    unknown = np.array(unknown)
    x = known[:, 0].reshape(-1, 1)
    y = known[:, 1].reshape(-1, 1)

    pred_x = unknown[:, 0].reshape(-1, 1)
    # print(pred_x)
    # print(X)
    # print(y)


    rf = AdaBoostRegressor(random_state=0, n_estimators=50)
    rf.fit(x, y)
    predicted = rf.predict(pred_x)
    index = 0
    print(known_pre)

    for i in range(len(data['price'])):
        if data['price'][i] != data['price'][i]:
            data['price'][i] = predicted[index]
            index = index + 1

    for i in range(len(data['price'])):
        if data['price'][i] != data['price'][i]:
            print(data['price'][i])
    five_number('price', data)
    plt.show()

def similarity(data):
    five_number('price', data)
    data['price'].plot.box()
    avg = data['price'].groupby(data['points']).mean()
    import math
    avg_new = avg.apply(lambda x: math.floor(x))
    print(avg_new)

    for i in range(len(data['price'])):
        if data['price'][i] != data['price'][i]:
            data['price'][i] = avg_new[data['points'][i]]
    five_number('price', data)
    plt.show()




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
    for row in data:
        print(row)
    # data = data["price"]
    # print(data)
    similarity(data)