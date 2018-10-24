import  numpy as np
import pandas as pd
from pandas import DataFrame as df
df = df(np.random.randn(5,3), #randn:기대값0, 표준편차1인 표준정규분포
   columns=['c1','c2','c3'])
print(df)

df.ix[0,0] = None
df.ix[1,['c1','c3']]= None
df.ix[1,['c1','c3']]=np.nan # None
df.ix[2,'c2'] = np.nan
df.ix[3,'c2'] = np.nan
df.ix[4,'c3'] = np.nan
print(df)

df_0 = df.fillna(0)
print(df_0)

df_missing = df.fillna('missing')
print(df_missing)
print(df)
print(df.fillna(method='ffill')) # ffill 바로 앞의 값을 따라감
print(df.fillna(method='pad')) # pad 바로 앞의 값을 따라감
print(df.fillna(method='bfill')) # bfill 바로 뒤의 값을 따라감
print("="*50)

print(df.fillna(method='ffill',limit=1)) #limit=1 Nan이 연속으로 여러개 나왔을 때 하나만 대체(시계열분석)
print(df.fillna(method='ffill',limit=2))
#
print(df.mean())
print(df.fillna(df.mean()))
print("="*50)
print(df.where(pd.notnull(df), df.mean(),
                          axis='columns'))
print("="*50)
print(df.mean()['c1'])
print(df.fillna(df.mean()['c1']))
print(df)
print("="*50)
print(df.mean()['c1':'c2'])
print(df.fillna(df.mean()['c1':'c2']))
print("="*50)

df_2 = pd.DataFrame({'c1':[1,2,3,4,5],
                     'c2':[6,7,8,9,10]})
print(df_2)
df_2.ix[[1,3],['c2']]=np.nan
print(df_2)

df_2['c2_new'] = np.where(pd.notnull(df_2['c2'])==True,df_2['c2'],df_2['c1']) #'c2'열의 값이 null이 아니라면(숫자가 있다면),'c2_new'에 c2값을 그대로 넣고, null이면 c1의 값을 가져옴
print(df_2)