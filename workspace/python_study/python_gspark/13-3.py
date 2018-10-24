#결측치 처리 & 데이터프레임 사용

# from pandas import DataFrame, Series
import pandas as pd
import numpy as np

pd.DataFrame()
# print(np.random.randn(5,3)) # n:normal distribution(표준정규분포), 평균(기대값):0, 표준편차:1
df = pd.DataFrame(np.random.randn(5,4),['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z'])
print(df)
print(type(df)) # DataFrame
print(df['W'])
print(type(df['W'])) # Series

print(df.drop('E'))
# df = df.drop('E')
# print(df)

print(df.shape)
print(df.loc['A']) # A행에 해당하는 열(column)의 값들 출력
print(df.iloc[0])
print(df.loc[['A','B']])
print(df.loc[['A','B'],['X','Y']]) #A,B행과 X,Y열이 교차하는 부분 출력

d = {'A':[1,2,np.nan],'B':[5,np.nan, np.nan], 'C':[1,2,3]} # nan:not a number(값이 없음)
print(d)
df = pd.DataFrame(d)
print(df)
print(type(df)) #DataFrame

print(df.dropna(axis=0)) #행이 삭제
print(df.dropna(axis=1)) #열이 삭제

print(df['A'].fillna(value="imsi"))
print(df.fillna(value="imsi"))
print(df)

# A열에 대해서 na값을 A열의 평균으로 대체
# print(df['A'].mean())
print(df['A'].fillna(value=df['A'].mean()))