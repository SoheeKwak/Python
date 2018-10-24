import pandas as pd
from pandas import DataFrame as df
import numpy as np

df_1 = df(data=np.arange(12).reshape(3,4),
          index=['r0','r1','r2'],
          dtype='int',
          columns=['c0','c1','c2','c3'])
print(df_1)
print(df_1.T) #Transpose
print(df_1.axes) #axis
print(df_1.dtypes)
print(df_1.size)
print(type(df_1)) #pandas.core.frame.DataFrame

print(df_1.values)
print(type(df_1.values)) #numpy.ndarray'
print("="*50)

df_2 = df({
    'class_1':['a','a','b','b','c'],
    'var_1':np.arange(5),
    'var_2':np.random.randn(5)},
    index=['r0','r1','r2','r3','r4'])
print(df_2)
print(df_2.index)
print(df_2.ix[2:]) #ix :행의 범위를 참조
print(df_2.ix[2]) #2번행 값만 출력
print("="*50)
print(df_2)
print(df_2.head(3)) #앞에서 3개 데이터 출력
print(df_2.tail(3)) #뒤에서 "

print(df_2.columns)
print(df_2['class_1'])

#class_1과 var_2컬럼 출력
print(df_2[['class_1', 'var_2']]) #두개 이상 출력할 때 [[]]

idx = ['r0','r1','r2','r3','r4']
df_1 = df({'c1':np.arange(5),
           'c2':np.random.randn(5)},
          index=idx)
print(df_1)

new_idx=['r0','r1','r2','r5','r6']
# df_1 = df_1.reindex(new_idx)
# print(df_1)
df_1 = df_1.reindex(new_idx, fill_value='missing')
print(df_1)

print(pd.date_range("2018-9-10", "2018-9-30", freq='B')) #freq='B':business day frequency,  http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-offset-aliases
print("="*50)
print(pd.date_range("2018-9-10", "2025-9-30", freq='MS')) #freq='MS': month start frequency

date_idx = pd.date_range("09/10/2018", periods=10, freq='D')
print(date_idx)
df_2 = df({"c1":[10,20,30,40,50,10,20,30,40,50]},
          index=date_idx)
print(df_2)

date_idx_2 = pd.date_range("09/05/2018", periods=20, freq='D')
print(date_idx_2)
# df_2 = df_2.reindex(date_idx_2, method='ffill') #df_2: 2018.9.10 ~ 9.19에 추가를 해준 값은 NaN으로 출력, method='ffill'는 바로 앞의 데이터를 그대로 따라가게 함
# print(df_2)
df_2 = df_2.reindex(date_idx_2, method='bfill') #method='bfill' 바로 뒤의 값을 따라감
print(df_2)