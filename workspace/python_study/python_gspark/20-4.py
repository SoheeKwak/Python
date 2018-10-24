import pandas as pd
import numpy as np
from pandas import DataFrame, Series

x = np.arange(18).reshape(3,6)
print(x)

print(np.hsplit(x,3)) #수평방향으로 3개로 나눈다
print(np.hsplit(x,(2,4))) #x[:,0:2], x[:,2:4], x[:,4:]

print(np.split(x,3,axis=1)) #print(np.hsplit(x,3))같음
print(np.split(x,(2,4), axis=1))
print("="*50)
x1,x2,x3 = np.hsplit(x,3)
print(x1)

print(x)
print(np.vsplit(x,3)) #수직으로 3개로 나뉨
print(np.split(x,3,axis=0))

# np.argmin(), np.argmax()
x = np.array([15,14,13,12,11,10])
print(x.min())
print(x.max())
print(np.max(x))
print(x.argmin())
print(x.argmax())
print(np.argmax(x))
#x배열에서 13이상인 색인의 위치를 출력
print(np.where(x>=13))
#x배열에서 13이상인 값들의 위치를 출력
print(x[np.where(x>=13)])
#x배열에서 13이상의 값은 모두 100으로 치환하고, 아니면 자기자신 그대로 x배열 출력
print(np.where(x>=13,100,x))
print("="*50)
x2 = []
for i in list(x): #array->list
    if i>=13:
        x2.append(100)
    else:
        x2.append(i)
print(x2) #list
x2 = np.asarray(x2) #list->array
print(x2)
print(type(x2))

x = np.array([1,2,3,1,2,4])
print(np.unique(x))

x = np.array([1,2,3,4])
y = np.array([3,4,6,5])
print(np.intersect1d(x,y)) #교집합
print(np.union1d(x,y)) #합집합
print(np.setdiff1d(x,y)) #차집합
print(np.setxor1d(x,y)) #대칭차집합

x = np.array([1,2,3,4,5,6])
y = np.array([2,4])
print(np.in1d(x,y)) #in1(숫자)d : x내부에서 y원소가 있나?

#배열 합치기
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)
#1)왼쪽에서 오른쪽으로 합치기 (좌우로 합체)
# np.r_[x,y] , np.hstack([x,y])
print(np.r_[a,b])
print(np.hstack([a,b]))

#2)위에서 아래쪽으로 합치기
#- np.r_[[x],[y]] , np.vstack([x,y])
print(np.r_[[a],[b]])
print(np.vstack([a,b]))

#3)두개의 1차원 배열 ->세로로 합치기->2차원 배열
#- np.c_[x,y] , np.column_stack([x,y])
print(np.c_[a,b])
print(np.column_stack([a,b]))