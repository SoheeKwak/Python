#데이터프레임 결측값 처리
#pandas에서는 결측값: Nan, None
import pandas as pd
from pandas import DataFrame as df
df_left = df({
    'a':['a0','a1','a2','a3'],
    'b':[0.5,2.2,3.6,0.4],
    'key':['k0','k1','k2','k3']})
df_right = df({
    'c':['c0','c1','c2','c3'],
    'd':['d0','d1','d2','d3'],
    'key':['k2','k3','k4','k5']})

df_all = df.merge(df_left,df_right,how='outer',on='key')
print(df_all)
print(pd.isnull(df_all))
print(df_all.isnull())

print(pd.notnull(df_all))
print(df_all.notnull())

print(df_all)
df_all.ix[[0,1],['a','b']] = None
print(df_all) #a:string형식 결측치=> None, b:float형식 경우 결측치=>NaN

print(df_all[['a','b']])
print(df_all[['a','b']].isnull())
print(df_all.isnull().sum())
print(df_all['a'].isnull().sum()) #isnull().sum() 열단위 결측값 개수
print(df_all.notnull().sum())
print(df_all.isnull().sum(1))
df_all['NaN_cnt'] = df_all.isnull().sum(1) # df_all.isnull().sum(1)행단위 결측값 개수
df_all['NotNull_cnt'] = df_all.notnull().sum(1)
print(df_all)

import numpy as np
from pandas import DataFrame
df = df(np.arange(10).reshape(5,2),
        index=['a','b','c','d','e'],
        columns=['c1','c2'])
print(df)
df.ix[['b','e'],['c1']]=None
df.ix[['b','c'],['c2']]=None
print(df)
print(df.sum()) # NaN은 0으로 처리
print(df['c1'].sum()) # NaN은 0으로 처리
print(df['c1'].cumsum()) #누적, NaN은 0으로 처리
print(df.mean()) #(0+4+6)/3, Nan은 제외, 열기준 평균
print(df)
print(df.mean(1)) #행기준 평균
print(df.std())
df['c3'] = df['c1']+df['c2'] #Nan이 하나라도 있으면 Nan
print(df)

df = DataFrame(np.arange(10).reshape(5,2),
        index=['a','b','c','d','e'],
        columns=['c1','c2'])
df2 = DataFrame({'c1':[1,1,1,1,1],
                 'c4':[1,1,1,1,1]},
        index=['a','b','c','d','e'])


print(df)
print(df2)
df['c3'] = df['c1']+df['c2']
print(df)
print(df+df2)

