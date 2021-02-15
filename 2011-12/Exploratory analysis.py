import pandas as pd
import numpy as np

# Import datasets
day = pd.read_csv("day.csv")
hour = pd.read_csv("hour.csv")

# check the shape of the datasets and look for any missing values
day.shape
# output: (731, 16)
hour.shape
# output: (17379, 17)

day.isnull().sum()
# output: 
# instant       0
# dteday        0
# season        0
# yr            0
# mnth          0
# holiday       0
# weekday       0
# workingday    0
# weathersit    0
# temp          0
# atemp         0
# hum           0
# windspeed     0
# casual        0
# registered    0
# cnt           0
# dtype: int64

hour.isnull().sum()
# instant       0
# dteday        0
# season        0
# yr            0
# mnth          0
# hr            0
# holiday       0
# weekday       0
# workingday    0
# weathersit    0
# temp          0
# atemp         0
# hum           0
# windspeed     0
# casual        0
# registered    0
# cnt           0
# dtype: int64
