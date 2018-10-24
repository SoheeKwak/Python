## 데이터프레임과 시리즈 합치기
import pandas as pd
from pandas import DataFrame as df
df_1 = df({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2'],
    'd':['d0','d1','d2']},
    index = [0,1,2])
Series_1 = pd.Series(['S1','S2','S3'],name='S')
print(Series_1)

print(pd.concat([df_1,Series_1]))
print("="*50)
print(pd.concat([df_1,Series_1],axis=1))
print(pd.concat([df_1,Series_1],axis=1,ignore_index=True))
print("="*50)

## Series끼리 합치기
Series_1 = pd.Series(['S1','S2','S3'],name='S')
Series_2 = pd.Series([0,1,2])
Series_3 = pd.Series([3,4,5])
print(pd.concat([Series_1,Series_2,Series_3]))
print(pd.concat([Series_1,Series_2,Series_3],axis=1))
print("="*50)
print(pd.concat([Series_1,Series_2,Series_3],axis=1,keys=['C0','C1','C2']))
print("="*50)

df_1 = df({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2'],
    'd':['d0','d1','d2']},
    index = [0,1,2])
Series_4 = pd.Series(['S1','S2','S3','S4'],index=['a','b','c','e'])
print(Series_4)
print(df_1.append(Series_4,ignore_index=True))

# DataFrame Join/Merge, 데이터 병합
df_left = df({
    'KEY':['a0','a1','a2','a3'],
    'b':['b0','b1','b2','b3'],
    'c':['c0','c1','c2','c3']})
df_right = df({
    'KEY':['a2','a3','a4','a5'],
    'd':['d0','d1','d2','d3'],
    'e':['e0','e1','e2','e3']})
print(df_left)
print(df_right)
print("="*50)
#KEY값이 같은 값들끼리 병합
df_merge_how_left = pd.merge(df_left,df_right)  #따로 KEY라고 지정해주지 않아도 공통된 것을 기준으로 교집합으로 병합됨
print(df_merge_how_left)
df_merge_how_left = pd.merge(df_left,df_right,how='left') #따로 KEY라고 지정해주지 않아도 공통된 것을 기준으로 교집합으로 병합됨
print(df_merge_how_left)
df_merge_how_left = pd.merge(df_left,df_right,how='left',on='KEY')
print(df_merge_how_left)
df_merge_how_left = pd.merge(df_left,df_right,how='right',on='KEY') #'KEY'오른쪽
print(df_merge_how_left)

df_merge_how_inner = pd.merge(df_left,df_right,how='inner',on='KEY') #KEY를 기준으로 교집합
print(df_merge_how_inner)

df_merge_how_outer = pd.merge(df_left,df_right,how='outer',on='KEY')
print(df_merge_how_outer)
df_merge_how_outer = pd.merge(df_left,df_right,how='outer',on='KEY',indicator=True)
print(df_merge_how_outer)



df_left = df({
    'KEY':['a0','a1','a2','a3'],
    'd':['b0','b1','b2','b3'],
    'c':['c0','c1','c2','c3']})
df_right = df({
    'KEY':['a2','a3','a4','a5'],
    'd':['d0','d1','d2','d3'],    #인덱스'd'가 공통적으로 있을 땐,  d_x, d_y로 나눠져서 출력
    'e':['e0','e1','e2','e3']})
df_merge_how_left = pd.merge(df_left,df_right,how='left',on='KEY')
print(df_merge_how_left)