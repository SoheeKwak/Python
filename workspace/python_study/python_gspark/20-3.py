#연속형 변수->기술통계량 집계 함수
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

df = DataFrame({'group':['a','a','a','b','b','b'],
                'value_1':np.arange(6),
                'value_2':np.random.randn(6)})
print(df)
grouped = df.groupby('group')
print(grouped)

print(grouped.count()) #그룹 내 non_NA(NA가 아닌 것)의 개수
print(grouped.sum()) #그룹 내 non_NA(NA가 아닌 것)의 값들의 합
print(type(grouped.sum())) #DataFrame
print(grouped.sum()['value_2'])
print(type(grouped.sum()['value_2'])) #Series
df2 = DataFrame(grouped.sum()['value_2'])
print(df2)
print(type(df2)) #DataFrame

print(df)
print("="*50)
# print(grouped.min())
# print(grouped.max())
print(grouped.mean())
print(grouped.median())
print(grouped.std())
print(grouped.var()) #분산
print(grouped.quantile(0.1)) #분위수(0~1사이의 값을 줄수 있음) (최대값-최소값에서 0.1(10%)위치에 해당하는 값)
print(grouped.first()) #그룹 내 첫번째 값
print(grouped.last()) #그룹 내 마지막 값
#
#그룹별 기술통계량
print(grouped.describe()['value_1'])
print(grouped.describe()['value_1'].T)
#
def iqr_func(x):                       #아래 그룹화된 변수를 iqr_func 함수를 불러
    q3, q1 = np.percentile(x,[75,25])  # 75%, 25%구간의 값을 x에 대입하여
    iqr = q3-q1                        #그 사이 구간을
    return iqr                        #iqr에 반환
print(grouped.aggregate(iqr_func))
# # print(grouped.agg(iqr_func))
#
print(grouped.quantile([0.75,0.25])) #위 함수와 같지만 더 편리함

#범주형 변수에서 특정 항목을 기준으로 매핑(dict.get())
df = DataFrame({
    'name':['kim','KIM','Kim','lee','LEE','Lee','park','choi'],
    'value':[1,2,3,4,5,6,7,8],
    'value_2':[100,300,200,100,100,300,50,80]
})
print(df)
# name 컬럼값 -> 새로운 그룹의 컬럼 생성('kim','lee','others')
name_mapping = {
    'KIM':'kim',
    'Kim':'kim',
    'LEE':'lee',
    'Lee':'lee',
    'park':'others',
    'choi':'others'
}
func = lambda x:name_mapping.get(x,x) # x를 넣었을 때 매핑되는 값이 없으면 그 자신x을 출력, ex) 'cho'->'cho'

df['name_2'] = df.name.map(func)
print(df)

print(df.groupby('name_2').sum())

print(df.groupby(['name_2','name'])['value_2'].sum())
