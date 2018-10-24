"""
집계함수(aggregate function:sum)
axis(축)지정. 기본값:None(전체)
1 2 3  2차선 행렬 구조이므로 axis가 두개
4 5 6
7 8 9
1)axis=None 행렬 전체를 하나의 배열로 보고 집계 연산(sum):45
2)axis=0 행 기준으로 각각의 행에 대한 동일한 인덱스의 요소를 하나의 배열로 보고 집계 연산 수행: 12, 115, 18
3)axis=1 열 기준으로 각각의 행에 대해 열값들에 대한 집계연산 수행:6, 15, 24
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.arange(1,10).reshape(3,3)
print(a)
print(np.sum(a, axis=None))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

print(np.max(a))
print(np.max(a, axis=0))
print(np.max(a, axis=1))
print(np.min(a, axis=0))
print(np.min(a, axis=1))

# cumsum():누적합계
print(np.cumsum(a))
print(np.cumsum(a, axis=0))
print(np.cumsum(a, axis=1))
print(a.cumsum(axis=0))

# median 중앙값
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
a = np.arange(1,5).reshape(2,2)
print(np.median(a)) # 2.5 짝수일때는 중앙값이 2,3사이의 값, 즉, 두개의 평균으로 나옴

a = np.arange(1,10).reshape(3,3)
print(a)
print(np.std(a))
print(np.std(a,axis=0))
print(np.std(a,axis=1))


a = np.arange(1,25).reshape(4,6)
b = np.arange(25,49).reshape(4,6)
print(a+b)
print(a+100)

new_arr = np.full_like(a,10)
print(a+new_arr)
print(a+10)

a = np.arange(5).reshape((1,5))  # 2차원
print(a)
b = np.arange(5).reshape((5,1)) # 2차원
print(b)
print(a+b)

a = np.random.randint(0,9,(3,3))
print(a)
a1 = np.copy(a)
a1[:,0] = 99
print(a1)

uns = np.random.random((3,3))
print(uns)
uns1 = uns
uns2 = uns
uns3 = uns
print("="*50)
uns1.sort() #각 행들이 오름차순으로 정렬됨, axis를 따로 정해주지 않으면 마지막 축(axis=-1)이 기준이 됨. 2차원에서는 열이 default, 3차원:depth가 기준
print(uns1)
uns1.sort(axis=1) #열을 기준으로 각 행들이 오름차순으로 정렬됨
print(uns1)
uns1.sort(axis=-1) #마지막 축 기준으로 각 행들이 오름차순으로 정렬됨
print(uns1)
uns1.sort(axis=0) # 각 열들이 정렬
print(uns1)

print("="*50)
a = np.array([40,30,10,20])
j = np.argsort(a)
print(j)
print(a[j])
print(np.sort(a))

print("="*50)
x = np.array([4,3,1,5,2,6,0])
print(np.sort(x)) #정렬 결과만 사본으로 리턴
print(x)
# np.sort(a, axis=0)[::-1]) #axis=0를 오름차순으로 정렬 후, 내림차순으로 정렬
xrev = np.sort(x)[::-1]
print(xrev)
# x.sort() #배열 자체가 정렬
# print(x)

print("="*50)
x = np.array([14,13,11,15,12,16,10])
print(np.argsort(x)) # [6 2 4 1 0 3 5]
print(np.argsort(-x)) # [5 3 0 1 4 2 6]
print(x[np.argsort(-x)]) # [16 15 14 13 12 11 10]

print("="*50)
arr = np.arange(0,2*3*4) #0~23(24개)
v = arr.reshape([2,3,4]) #3차원: 행row2 열col3 깊이depth4
print(v)

print(v.sum())
print(v.ndim)
res1 = v.sum(axis=0) #2*3*4 => 3*4
print(res1)

res2 = v.sum(axis=1)
print(res2.shape) #2*3*4 => 2*4
print(res2)

res3 = v.sum(axis=2)
print(res3.shape) #2*3*4 => 2*3
print(res3)