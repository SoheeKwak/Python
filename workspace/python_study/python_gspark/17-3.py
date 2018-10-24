import pandas as pd
from pandas import DataFrame as df
df_left_2 = df({
    'KEY':['a0','a1','a2','a3'],
    'a':['b0','b1','b2','b3'],
    'b':['b0','b1','b2','b3'],
    'c':['c0','c1','c2','c3']})
df_right_2 = df({
    'KEY':['a2','a3','a4','a5'],
    'b': ['b0', 'b1', 'b2', 'b3'],
    'c':['d0','d1','d2','d3'],
    'd':['e0','e1','e2','e3']})

print(pd.merge(df_left_2,df_right_2,how='inner',on='KEY',suffixes=('_left','_right')))

df_left = df({
    'a':['a0','a1','a2','a3'],
    'b':['b0','b1','b2','b3']},
    index=['k0','k1','k2','k3'])
df_right = df({
    'c':['c0','c1','c2','c3'],
    'd':['d0','d1','d2','d3']},
    index=['k2','k3','k4','k5'])
#인덱스 기준으로 데이터프레임 합치는 작업
print(pd.merge(df_left,df_right,
               left_index=True,right_index=True,how='left'))
# print(df_left.join(df_right,how='right'))
# print(df_left.join(df_right,how='inner'))
# print(df_left.join(df_right,how='outer'))
