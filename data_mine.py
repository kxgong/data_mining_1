import numpy
import csv
from collections import Counter
import numpy as np
import pandas as pd
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

root = '../youtube_trending/'
csv_list = ['CAvideos.csv', 'DEvideos.csv', 'FRvideos.csv', 'GBvideos.csv', 'INvideos.csv', 'JPvideos.csv',
            'KRvideos.csv', 'MXvideos.csv', 'RUvideos.csv', 'USvideos.csv']

# for i in range(len(csv_list)):
#     path = root + csv_list[i]
#     data = pd.read_csv(path)
#     # print(data)
#     print(path)
#     #print(data.dropna(thresh=1))
#     # for row in data:
#     #     print(row)
#     # print(data["category_id"])
#     counter_category = Counter(data["category_id"])
#     print(counter_category)
#
#     counter_channel_title = Counter(data['channel_title'])
#     print(counter_channel_title)
#
#
#     five_number("views", data)
#
#     five_number("likes", data)
#
#     five_number("dislikes", data)
#
#
path = "../wine_review/winemag-data_first150k.csv"
data = pd.read_csv(path)
print(path)
#
# counter_country = Counter(data["country"])
# print(counter_country)
#
# counter_designation = Counter(data['designation'])
# print(counter_designation)
#
# counter_province = Counter(data['province'])
# print(counter_province)
#
# counter_region_1 = Counter(data['region_1'])
# print(counter_region_1)
#
# counter_region_2 = Counter(data['region_2'])
# print(counter_region_2)
#
# counter_variety = Counter(data['variety'])
# print(counter_variety)
# #
# counter_winery = Counter(data['winery'])
# print(counter_winery)




five_number("points", data)

five_number("price", data)

# counter_title = Counter(data["title"])
# print(counter_title)

# counter_publish_time = Counter(data["publish_time"])
# print(counter_publish_time)
#
# counter_tags = Counter(data["tags"])
# print(counter_tags)

# counter_comments_disabled = Counter(data["comments_disabled"])
# print(counter_comments_disabled)
#
# counter_ratings_disabled = Counter(data["ratings_disabled"])
# print(counter_ratings_disabled)


#     print(data[str(row)])
#     print(data[str(row).dropna(how="all")])

# for i in range(len(data)):
#     print(i)
# print(data.head(5))