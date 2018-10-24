import pandas as pd
from pandas import DataFrame as df

df_1 = df({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2'],
    'd':['d0','d1','d2']},
    index = [0,1,2])
df_2 = df({
    'a':['a3','a4','a5'],
    'b':['b3','b4','b5'],
    'c':['c3','c4','c5'],
    'd':['d3','d4','d5']},
    index = [3,4,5])
print(df_1)
print(df_2)
#concat 데이터프레임 합치는 함수 (cf. R언어:rbind, cbind)
df_12_axis0 = pd.concat([df_1,df_2]) # default:axis=0
print(df_12_axis0)
print("="*50)

df_3 = df({
    'e':['e0','e1','e2'],
    'f':['f0','f1','f2'],
    'g':['g0','g1','g2'],
    'h':['h0','h1','h2']},
    index = [0,1,2])
df_13_axis1 = pd.concat([df_1, df_3], axis=1)
print(df_13_axis1)
print("="*50)
df_4 = df({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2'],
    'e':['e0','e1','e2']},
    index = [0,1,3])
# df1과 df4를 outer_join(외부 조인)수행
print(df_1)
print(df_4)
df_14_outer = pd.concat([df_1,df_4],join='outer') # join='outer' 두 데이터프레임의 컬럼에 대한 합집합
print(df_14_outer)
df_14_inner = pd.concat([df_1,df_4],join='inner') # join='inner' 교집합
print(df_14_inner)
print("="*50)

#axis=1, index를 그대로 사용할 때:join_axes
df_14_outer_axis1 = pd.concat\
    ([df_1,df_4], join='outer', axis=1) # join='outer'axis=1 두 데이터프레임의 행에 대한 합집합
print(df_14_outer_axis1)

df_14_inner_axis1 = pd.concat\
    ([df_1,df_4], join='inner', axis=1) # join='inner'axis=1 두 데이터프레임의 행에 대한 교집합
print(df_14_inner_axis1)
print("="*50)

df_14_join_axes_axis1 = pd.concat\
    ([df_1,df_4], join_axes=[df_1.index], axis=1) #df_1.index : df_1의 index를 기준으로 함
print(df_14_join_axes_axis1)