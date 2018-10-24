import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import DataFrame
df = DataFrame({'c1':[0,1,2,3],
                'c2':[4,5,6,7],
                'c3':[8,9,10,np.nan]},
                index = ['r1','r2','r3','r4'])
print(df.index)
print(df.columns)

df_r1 = DataFrame(df,index=['r1','r3'])
print(df_r1)
df_c1 = DataFrame(df,columns=['c1','c3'])
# print(df_c1)
# #기존의 데이터프레임으로부터 원하는 특정부분만 추출하여 새로운 데이터프레임 생성
df_ex = DataFrame(df,
                  index=['r3','r1'],
                  columns=['c3','c1'])
print(df_ex)

#데이터프레임 찹조
print(df[['c1','c3']])
df['csum'] = df['c1']+df['c2']
print(df)
df = df.assign(cmul=df['c1']*df['c2'])
print(df)
df = df.assign(cmul2=lambda x: x.c1 * x.c2)
print(df)

print(df.drop(['cmul','cmul2'],1)) #열 제거시 axis=1
print(df.drop(['r1','r3'])) #행 제거는 그냥
del df['csum']
print(df)

print(df['c1'])
print(df.c1)
print(df[0:2])
print(df['c1'][0:2])
print(df.c1[0:2])
print(df.loc['r1'])
print(df)
print(df.loc[['r1','r2']])
print(df.iloc[0:2])
print(df[0:2])
print(df[df['c1']<=1])
#
s = ['c1','c2']
print(df[s])