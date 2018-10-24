import pandas as pd
import numpy as np
from pandas import DataFrame, Series

#ravel:다차원 배열-> 1차원 배열
x = np.arange(12).reshape(3,4)
print(x)
print(np.ravel(x,order='C')) #default, 칼럼순으로 배열
print(np.ravel(x,order='F')) #아래순으로 배열
# print(np.ravel(x,order='K')) #메모리 저장순(사용x)

y = np.arange(12).reshape(2,3,2) #3차원
print(y)
print(np.ravel(y,order='C')) #1차원

import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.ylabel('some numbers')
# plt.show()

data = {
    'a':np.arange(50),
    'c':np.random.randint(0,50,50),
    'd':np.random.randn(50)
}
# data['b'] = data['a']+10*np.random.randn(50) #기존 딕셔너리에 키'b'추가
# data['d'] = np.abs(data['d'])*100 #기존 키'd'를 변경(abs:절대값으로 바꾸므로 양수로만 출력)
# print(data)
#
# plt.scatter('a','b', c='b', s='d', data=data) # c:color, s:size
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()


mu,sigma = 100,15
x = mu + sigma*np.random.randn(10000) #모집단에서 평균100, 표준편차가 15인 표본 10000개를 추출하라
n, bins, patches = plt.hist(x,bins=50,density=1) #구간50개, density(확률밀도1=100%) ->그래프 상 평균100이 0.028정도의 비율로 나옴. 즉, 약 2.8%정도. 이 10000개를 모두 합하면 1
print("n=",n)
plt.title("histogram")
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()