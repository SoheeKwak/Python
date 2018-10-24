import numpy as np
import pandas as pd
from pandas import DataFrame as df, Series
from datetime import datetime

df = df(np.random.randn(5,4),
        columns=['c1','c2','c3','c4'])
print(df)
df.ix[2,'c2']=np.nan
df.ix[[0,1],'c1']=None
print(df)

df_drop_row = df.dropna(axis=0) #결측값이 있는 행 전체를 제거
print(df_drop_row)

df_drop_column = df.dropna(axis=1) #결측값이 있는 열 전체를 제거
print(df_drop_column )
print("="*50)
print(df)
print("="*50)
print(df['c1'].dropna()) #'c1'에 대해서만 NaN이 있는 행을 제거
print(df[['c1','c2','c3']].dropna()) #c1,c2,c3를 하나로 보고 전체행에 대해서 NaN이 있는 행은 모두 제거
print(df[['c1','c2','c3']].dropna(axis=1))
print(df.ix[[2,4],['c1','c2','c3']].dropna(axis=0)) #2행, 4행에 대해

datestrs = ['9/11/2018','9/12/2018','9/13/2018','9/14/2018'] #월/일/연도
dates = pd.to_datetime(datestrs)
print(dates)
#
ts = Series([1,np.nan,np.nan,10],index=dates)
print(ts)
# ts_intp_linear = ts.interpolate()
# print(ts_intp_linear)

datestrs = ['9/11/2018','9/13/2018','9/14/2018','9/20/2018']
dates = pd.to_datetime(datestrs)
print(dates)

ts = Series([1,np.nan,np.nan,10],index=dates)
print(ts)
ts_intp_linear = ts.interpolate(method='time') #날짜index인 경우, method='time'설정하면 시간의 흐름에 따른 값으로 보간
print(ts_intp_linear)

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
df =  DataFrame({'c1':[1,np.nan,np.nan,10],'c2':[1,3,np.nan,10]})
df_v = df.interpolate(method='values')
print(df_v)

#fillna: 결측값 대체
#replace:결측값 뿐만 아니라 모든값 대체
ser = Series([1,2,3,4,np.nan])
print(ser)
ser = ser.replace(2,20) #2를 20으로 대체
print(ser)
ser = ser.replace(np.nan,5)
print(ser)
print(ser.replace([1,2,3,4,np.nan]),[6,7,8,9,10])  #[1,2,3,4,np.nan]리스트 전체를 [6,7,8,9,10]로 대체
print(ser.replace({1:6,
                   2:8,
                   3:9,
                   4:7,
                   np.nan:10})) #딕셔너리도 값 값에 대응한 값으로 대체 가능
df = DataFrame({'c1':['a_old','b','c','d','e'],
                'c2':[1,2,3,4,5],
                'c3':[6,7,8,9,np.nan]})
print(df)
print(df.replace({'c1':'a_old'},{'c1':'a_new'}))
print(df.replace({'c3':np.nan},{'c3':10}))
#
data = {'key1':['a','b','b','c','c'],
        'key2':['v','w','w','x','y'],
        'col':[1,2,3,4,5]}
df = pd.DataFrame(data)
print(df)

print(df.duplicated(['key1'])) #중복된 것인가?
print(df.duplicated(['key1'],keep='first'))
print(df.duplicated(['key1'],keep='last'))
print(df.duplicated(['key1','key2']))#key1, key2를 하나로 봄
print(df.duplicated(['key1'],keep=False)) #중복된 것은 전부

# #1개만 남기고 나머지 중복은 제거
print(df)
print(df.drop_duplicates(['key1'],keep='first'))
print(df.drop_duplicates(['key1'],keep='last')) #중복될 때 마직막 것이 남고 앞에 것이 제거
print(df.drop_duplicates(['key1'],keep=False)) #중복된 것은 전부 제거