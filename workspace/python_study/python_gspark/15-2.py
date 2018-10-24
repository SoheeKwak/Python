import numpy as np
a1 = np.arange(24)
a2 = np.arange(24).reshape((4,6))
a3 = np.arange(24).reshape((2,4,3))
a1[5]=1000
a2[0,1]=1000
a3[1,0,1]=1000 #2번째 행, 1번째열, 2번째depth

print(a1)
print(a2)
print(a2[1:3,1:5])
print(a2[1:-1,1:-1])
print(a2[:,1:3])
a2[:,1:3]=99
print(a2)

a1 = np.arange(1,25).reshape(4,6)
even_a = a1%2==0
print(a1[even_a])
print("="*50)

import pandas as pd

rain = pd.read_csv("seattle.csv")
print(rain)
print("="*50)
rain_r = rain['PRCP']
print(rain_r)
print(type(rain_r)) #<class 'pandas.core.series.Series'>
print("="*50)
rain_r = rain['PRCP'].values
print(rain_r)
print(type(rain_r)) #<class 'numpy.ndarray'>
print("데이터 크기:",len(rain_r))
days_a = np.arange(0,365)
con_jan = days_a < 31 #True:31개 False:334개
print(con_jan[:40]) #1월1일부터 40일간의 강수량 데이터
print("="*50)
print(con_jan) #1월 한달간(31일간) 강수량 데이터
print(np.sum(rain_r[con_jan]))#1월달 강수량의 총합
print(np.mean(rain_r[con_jan])) #1월달 평균 강수량

a = np.arange(1,25).reshape((4,6))
# 팬시 인덱싱: 배열에 인덱스 배열을 전달해서 데이터를 참조
print(a)
print(a[0,0],a[1,1],a[2,2],a[3,3])
print(a[[0,1,2,3],[0,1,2,3]])
print(a[:,[1,2]])#대괄호 안에 콜론없이 지정되면 범위가 아닌, 그 해당 열만 출력
print(a[:,[1,3]])

print("="*50)
#ravel(배열을 1차원으로)
a = np.random.randint(1,10,(2,3))
print(a)
print(a.ravel())

#resize:배열크기 변경(요소 수 변경), reshape:배열변경(요소 수 변경X)
print(a.shape)
a.resize((2,2))
print(a)

print("="*50)
a = np.random.randint(1,10,(2,6))
print(a)
a.resize((2,10)) #사이즈가 커지면 늘어난 요소만큼 채워지고 0으로 초기화
print(a)
a.resize((3,3)) # 사이즈가 줄어들면 순서대로 요소가 들어가고 나머지 삭제됨
print(a)
print("="*50)

a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
res = np.append(a,b)
print(res) #1차원으로 출력
print(a)
print(b)
print("="*50)
res = np.append(a,b, axis=0) #행방향 2차원 배열
print(res)
print("="*50)

a = np.arange(1,10).reshape(3,3)
res = np.arange(10,20).reshape(2,5)
b = np.arange(10,19).reshape(3,3)
# np.append(a,res,axis=0) #기준축과 Shape다르면 append 오류 발생
# print(res)
print(a)
res = np.append(a,b,axis=1) #열방향, 2차원 배열
print(res)
print(b)
res = np.append(a,b,axis=0) #행방향, 2차원 배열
print(res)
# x = np.arange(10,20).reshape(2,5)
# np.append(res,x,axis=1) #shape이 다르므로 오류

a = np.arange(1,10).reshape(3,3)
print(a)
a = np.insert(a,3,99) #1차원, 99를 3번째 자리에 넣어라
print(a)
a = np.arange(1,10).reshape(3,3)
a = np.insert(a,2,99, axis=0) #행을 따라 2번째 줄에 99를 추가로 넣어라
print(a)
a = np.arange(1,10).reshape(3,3)
a = np.insert(a,1,99, axis=1) #열을 따라 2번째 줄에 99를 추가로 넣어라
print(a)

print("="*50)
a = np.arange(1,10).reshape(3,3)
print(a)
print(np.delete(a,3)) #1차원, 3번째 자리 요소를 지워라

#a배열의 1번 인덱스 행 제거한 후 출력
print(np.delete(a,1,axis=0))
#a배열의 1번 인덱스 열 제거한 후 출력
print(np.delete(a,1,axis=1))
print("="*50)

#배열 간의 결합(concatenate, vstack, hastack)
a = np.arange(1,7).reshape(2,3)
print(a)
b = np.arange(7,13).reshape(2,3)
print(b)
res = np.concatenate((a,b))
print(res)
print("="*50)

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
print(np.vstack((a,b)))
print(np.vstack((a,b,a,b))) #vertical 수직방향으로 붙음

print("="*50)
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
print(np.hstack((a,b)))  #horizontal 수평방향으로 붙음
print(np.hstack((a,b,a,b,a,b)))

print("="*50)
a = np.arange(1,25).reshape(4,6)
print(a)
res = np.hsplit(a,2) #a를 두개의 그룹으로 좌우로 나눔
print(res)
res = np.hsplit(a,3)
print(res)
res = np.vsplit(a,2) #a를 두개의 그룹으로 상하로 나눔
print(res)
#
print("="*50)
x = np.array([1,2])
print(x)
print(x.dtype)
x = np.array([1.,2.])
print(x.dtype)
x = np.array([1,2],dtype=np.int64)
print(x.dtype)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11,12])
#벡터의 내적
print(np.dot(v,w)) #9*11+10*12=219
print(v.dot(w))
#행렬과 벡터의 곱
print(x.dot(v)) #[1,2]*[9,10]+[3,4]*[9,10]=[29,67]
#행렬곱
print(x)
print(y)
print(np.dot(x,y)) #1*5+2*7, 1*6+2*8, 3*5+4*7, 3*6+4*8

x = np.array([[1,2],[3,4]])
print(x)
print(x.T) #transpose 대칭되는 요소끼리 묶어줌
print("="*50)

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(x)
v = np.array([1,0,1])
y = np.empty_like(x) #x와 같은 shape을 만들어 준다
print(y)
print("="*50)
for i in range(4):
    y[i,:] = x[i,:]+v #[2,2,4]=[1,2,3]+[1,0,1]
print(y)
print("="*50)
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
vv = np.tile(v,(4,1)) #열방향으로 v를 4번 반복
print(vv)
vv = np.tile(v,(4,2))
print(vv)
vv = np.tile(v,(4,5))
print(vv)

a = np.array([[1,2],[4,5]])
s = np.prod(a) #각각의 요소에 대해 곱셈
print(s)
s = np.prod(a,axis=0)
print(s)
s = np.prod(a,axis=1)
print(s)
s = np.max(np.prod(a,axis=1))
print(s)







