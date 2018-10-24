import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

obj = Series([1,2,-3,4])
print(obj)
print(obj.values) #값만 추출
print(obj.index) #인덱스 추출

obj = Series([1,2,-3,4], index=['x','y','z','k'])
print(obj)
print(obj['y'])

obj['x']= 10
print(obj)

print(obj[['x','y','z']]) #2개 이상의 인덱스를 참조할 때는 [[]]대괄호를 하나 더 써줌
print("="*50)
print(obj>0)
print((obj[obj>0])) #위에서 True값만 추출
print(obj*2)
print(np.exp(obj))

#null(초기화되지 않은 상태), na(결측치)
print(obj)
print('a' in obj)
print('x' in obj)
print("="*50)

sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = Series(sdata)
print(obj3)
print(type(obj3))

states = ['California','Ohio','Oregon','Texas']
obj4 = Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
#일반적으로 nan:숫자가 아닌 문자 같은 것
#na:값이 누락, null:값이 초기화 되지 않은 상태
#but, Pandas의 개념은, isnull함수: na(null, nan)인지 아닌지 확인하는 함수로 쓰임

print(obj3+obj4)
print("="*50)
obj4.name = 'population'

print(obj4)
obj.index.name = 'state'
obj4.index = ['w','x','y','z']
print(obj4)

data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame = DataFrame(data)
print(frame)
frame = DataFrame(data, columns=['year','state','pop'])
print(frame)

frame2 = DataFrame(data, columns=['year','state','pop','debt'],
          index=['one','two','three','four','five'])
print(frame2)
print(frame2['state'])
print("="*50)
print(frame2[['state','year']])
print(frame2.ix[['three','five']])

print(frame2)
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(5) #DataFrame은 인덱스 길이가 같아야 함
print(frame2)

val = Series([-1.2, -1.5, -1.7],
             index=['two','four','five']) #Series의 경우, 위 DataFrame과 달리, 길이가 같지 않아도 가능
frame2['debt']=val                         #즉, 길이가 다은 데이터 열을 추가 시->시리즈를 생성하여 추가
print(frame2)

frame2['eastern']=frame2.state=='Ohio'
print(frame2)

del frame2['eastern'] # del 제거
print(frame2)
print(frame2.columns)
print(frame2.index)

pop = {'Nevada':{2001:2.4, 2002:2.9},
       'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
frame3 = DataFrame(pop) # 바깥에 있는 키 Nevada  Ohio 가 열로 오게 됨
print(frame3)
print(frame3.T) #Transpose:행렬을 바꿔줌

frame4 = DataFrame(frame3, index=[2001,2002,2003]) #인덱스로 지정해 준 것이 행으로 가게 됨
print(frame4)
print("="*50)
print(frame3)
pdata = {'Ohio':frame3['Ohio'][:-1], #Ohio키에 frame3의 Ohio열만 가져와서 마지막줄 전까지만 추출
         'Nevada': frame3['Nevada'][:2]}
frame5 = DataFrame(pdata)
print(frame5)