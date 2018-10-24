import pandas as pd
from pandas import DataFrame as df, Series

df_left = df({
    'a':[1,2,3,4,5],
    'b':['b0','b1','b2','b3','b4'],
    'c':['c0','c1','c2','c3','c4'],
    'f':['f0','f1','f2','f3','f4'],
    'g':['g0','g1','g2','g3','g4']})
df_right = df({
    'r':[4,5,6,7,8],
    'd':['d0','d1','d2','d3','d4'],
    'e':['e0','e1','e2','e3','e4'],
    'k':['k2','k3','k4','k5','k6'],
  'top':[1,2,3,4,5]})
print(df_left)
print(df_right)

print(pd.merge(df_left,df_right,left_index=True,right_index=True))

import random

df_1st_half = df({
    'sales':[random.randrange(1000000) for _ in range(6)],
    'cost': [random.randrange(1000000) for _ in range(6)]},
    index = ['m1','m2','m3','m4','m5','m6'])
# print(df_1st_half)

df_2nd_half = df({
    'sales':[random.randrange(1000000) for _ in range(6)],
    'cost': [random.randrange(1000000) for _ in range(6)]},
    index = ['m7','m8','m9','m10','m11','m12'])
# print(df_2nd_half)

df_year = pd.concat([df_1st_half,df_2nd_half])

df_year['profit'] = df_year['sales'] - df_year['cost']
df_year.ix['results'] = [sum(df_year['sales']),sum(df_year['cost']),sum(df_year['profit'])]
print(df_year)

import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(x[x%3==0])
print(x[x%4==1])
print(x[(x%3==0) & (x%4==1)])