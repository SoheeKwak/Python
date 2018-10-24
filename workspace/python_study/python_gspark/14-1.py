import numpy as np
print(np.__version__)

list1 = [1,2,3,4]
a = np.array(list1)
print(a) # [1 2 3 4]
print(a.shape) # shape:(4,)=> rank:1
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape) # shape:(2, 3) 2행 3열, rank:2
print(b[0,0])
print(a[2])
print(type(b)) #<class 'numpy.ndarray'> 자료구조
print(type(list1)) #<class 'list'>

# 벡터화 연산#
#배열의 각 요소에 대한 반복연산을 하나의 명령으로 수행하기 때문에 속도가 빠름

data = [1,2,3,4,5]
ans = []
for i in data:
    ans.append(2*i)
print(ans)  #[2, 4, 6, 8, 10]

#위와 비교되는  벡터화 연산(for 반복문 없음, 속도 훨씬 빠름)
x = np.array(data)
print(2*x) # [ 2  4  6  8 10] 벡터화 연산으로 각 요소를 두배
print(2*data) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5] 리스트를 두배

a = np.array([1,2,3])
b = np.array([10,20,30])
print(a*2+b)
print(a==2)
print(b>10)
print((a==2)&(b>10))
print(a.shape)
print(a.ndim) #rank 출력
print(a.dtype) #int32:자료형, 4바이트 크기의 정수 저장

a = np.zeros(4) #[0. 0. 0. 0.]
print(a)
print(a.dtype) # float64: 자료형, 8바이트 실수 저장

a = np.zeros((2,2)) # 2행2열을 0으로 채워라
print(a)
a = np.ones((2,3)) # 2행3열을 1로 채워라
print(a)
a = np.full((2,3), 5) # 2행3열을 5로 채워라
print(a)
a = np.eye(5) #단위행렬: 대각요소값 1 나머지 0: 동일한 구조의 행렬을 곱했을 때 자기자신이 나오는 항등원 행렬
print(a)

print(range(20))
print(np.array(range(20)).reshape(4,5)) #1차원(20,) => 2차원(4,5)
c = np.array(range(20)).reshape(4,5)
print(len(c)) # 행의 개수
print(len(c[0])) #0번 행의 길이, 즉 열의 개수
print(c.ndim) #rank:2

print(c)
print(c>10) # True or False
print(c[c>10]) #[11 12 13 14 15 16 17 18 19]

c[c>10]=99 #10보다 큰 요소들에 99를 대입한다.
print(c)

arr = np.arange(0, 3*2*4) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
print(arr)
print(len(arr)) # 24
v = arr.reshape([3,2,4]) # depth:3, 2행4열
print(v)
print(len(v)) # 3
print(len(v[0])) # 2
print(len(v[0][0])) # 4


