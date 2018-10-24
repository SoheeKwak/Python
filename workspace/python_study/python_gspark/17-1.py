## 데이터프레임 합치기
import pandas as pd
from pandas import DataFrame as df
#index 무시: ignore_index
df_5 = df({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2'],
    'd':['d0','d1','d2']},
    index = ['r0','r1','r2'])
df_6 = df({
    'a':['a3','a4','a5'],
    'b':['b3','b4','b5'],
    'c':['c3','c4','c5'],
    'd':['d3','d4','d5']},
    index = ['r3','r4','r5'])

df_56_with_index = pd.concat([df_5,df_6])
print(df_56_with_index)

df_56_with_index = pd.concat([df_5,df_6], ignore_index=True)
print(df_56_with_index)

df_56_with_index = pd.concat([df_5,df_6], ignore_index=False,keys=['df5','df6'], names=['df_name','row_number'])  #keys 계층구조
print(df_56_with_index)
print("="*50)

print(df_56_with_index.ix['df5'])
print(df_56_with_index.ix['df5'][0:2])
print("="*50)

df_7 = df({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2'],
    'd':['d0','d1','d2']},
    index = ['r0','r1','r2'])
df_8 = df({
    'a':['a3','a4','a5'],
    'b':['b3','b4','b5'],
    'c':['c3','c4','c5'],
    'd':['d3','d4','d5']},
    index = ['r2','r3','r4'])
df_78 = pd.concat([df_7,df_8],verify_integrity=False) #verify_integrity=False 무결성검증을 하지 않겠다(여기선 이게 생략되어도 결과 같음), True일 시 중복되는 인덱스'r2'때문에 에러가 남
print(df_78)