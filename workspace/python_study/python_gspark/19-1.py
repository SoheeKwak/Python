#연속형 변수 -> 이산화(2개 이상의 범주로 변환)
import numpy as np
import pandas as pd
from pandas import DataFrame
np.random.seed(777)

df = DataFrame({'c1':np.random.randn(20),
           'c2':['a','a','a','a','a','a','a','a','a','a',
                 'b','b','b','b','b','b','b','b','b','b']})
print(df)
#c1을 최소값~최대값 구간 10개로 균등하게 분할
# print(np.linspace(1,2,10)) #1부터2사이의 구간을 10개로 분할
bins = np.linspace(df.c1.min(), df.c1.max(),10)
print(bins)
df['c1_bin'] = np.digitize(df['c1'],bins) #digitize:c1을 bins의 기준에 의해 10등분으로 분할하여 번호를 매긴다.
print(df)

print(df.groupby('c1_bin')['c1'].size()) #그룹화를 했을 때 각열의 데이터가 몇개가 있나?
print(df.groupby('c1_bin')['c1'].mean())
print(df.groupby('c1_bin')['c1'].std())
print(df.groupby('c1_bin')['c2'].value_counts())
print(df[df['c1_bin']==2])

print(df)
print("="*50)
print(pd.get_dummies(df['c1_bin'],prefix='c1')) #prefix(접두사)뒤에 df['c1_bin']구간 10개가 칼럼으로 옴. get_dummies:각각의 데이터가 어느 구간에 속하는지를 보여줌

print(df.c1.mean())
df['high_low'] = np.where(df['c1']>=df.c1.mean(),'high','low') #c1의 값이 평균보다 높으면 high, 그렇지 않다면 low
print(df)
print(df.groupby('high_low'))

Q1 = np.percentile(df['c1'],25) # 25%위치 = Q1
Q3 = np.percentile(df['c1'],75) # 75%위치 = Q3
print(Q1)
print(Q3)
df['h_m_1'] = np.where(df['c1']>=Q3,'01_high',
         np.where(df['c1']>=Q1,'02_medium','03_low')) #중첩조건
print(df)

