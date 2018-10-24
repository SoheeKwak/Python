import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.ones_like(a)
print(b)
c = np.zeros_like(a)
print(c)

# 데이터 생성 함수
a = np.linspace(0,1,5) # 0~1범위 내에서 균등 간격으로 5개의 수를 생성
print(a)
# a = np.linspace(0,100) #특별히 수를 안 정해주면 50개로 default
# print(a)
import matplotlib.pyplot as plt
# plt.plot(a,'o') #따로 지정해주지 않으면 y값으로 출력하고, x값은 자동으로 0,1,2,3,4..
# plt.show()

# a = np.arange(10)
# print(a)
# a = np.arange(0,10,2)
# print(a)
a = np.arange(0,10,2,np.float)
print(a)
# plt.plot(a,'o') #따로 지정해주지 않으면 y값으로 출력하고, x값은 자동으로 0,1,2,3,4..
# plt.show()

#정규분포 random.normal
mean = 0
std = 1
a = np.random.normal(mean, std, (2,3)) #평균0을 중심으로 1씩 표준편차인 2행3열 정규분포
print(a)
a = np.random.normal(mean, std, 10000) #평균0을 중심으로 1씩 표준편차인 10000개
print(a)
plt.hist(a,bins=100) # bins:y좌표 빈도수
plt.show()
plt.hist(a,bins=10)
plt.show()

#균등분포(0이상 1미만 난수)
a = np.random.rand(10000)
plt.hist(a,bins=10)
plt.show()

a = np.random.randint(5,10,size=(3,4)) #5이상10미만 랜덤으로 3행4열 추출
print(a)

a = np.random.randint(-100,100,size=10000)
print(a)
plt.hist(a,bins=10)
# plt.show()
#
#
#
a = np.random.randint(0,10,(2,3))
print(a)
b = np.random.randint(0,10,(2,3))
print(b)

np.save("myarr1", a) #myarr1.npy 파일 생성, save():배열을 바이너리 형태로 저장
np.savez("myarr2", a,b) #myarr2.npy 파일 생성, savez():배열을 바이너리 형태로 저장
print("myarr1=", np.load("myarr1.npy"))
print("myarr2=", np.load("myarr2.npz"))

npzfiles = np.load("myarr2.npz")
print(npzfiles.files)
print(npzfiles['arr_0'])
print(npzfiles['arr_1'])

print(np.loadtxt("simple.csv",dtype=np.int))

data = np.loadtxt("height.csv", delimiter=",", skiprows=1, dtype={
    'names':("order","names","height(cm)"),
    'formats':('i','S20','f')
     })
print(data)

data = np.random.random((3,4))
print(data)
np.savetxt("saved.csv", data, delimiter=",") #배열을 텍스트 파일로 저장
print(np.loadtxt("saved.csv", delimiter=","))

# arr = np.random.random((5,2,3))
# print(arr)
# print(len(arr))
# print(type(arr)) # float64
# print(arr.ndim)
# print(arr.size) #요소의 총수
# print(arr.dtype)
# arr = arr.astype(np.int) # 타입 변경
# print(arr.dtype) # int32
# print(arr)
# arr = arr.astype(np.float) #타입 변경
# print(arr)
# print(arr.dtype) #float64
# print(np.info(np.ndarray.dtype))
#
# a = np.arange(1,10).reshape(3,3)
# print(a)
# b = np.arange(9,0, -1).reshape(3,3) #감소 시 얼마나 감소하는지 반드시 명시
# print(b)
#
# print(a-b)
# print(np.subtract(a,b))
#
# print(a+b)
# print(np.add(a,b))
#
# print(a/b)
# print(np.divide(a,b))
#
# print(a*b)
# print(np.multiply(a,b))
#
# # print(b)
# # print(np.exp(b)) #자연상수
# # print(a)
# # print(np.sqrt(a)) # 제곱근
# # print(np.sin(a)) #싸인 함수
# # print(np.cos(a))
# # print(np.tan(a))
# # print(np.log(a))
#
#
#
# print(a==b)
# print(np.array_equal(a,b)) #행렬 전체가 완전히 같은가? 하나라도 다른 요소가 있다면 False
#
# print(a.sum()) # axis
# print(np.sum(a))
# print(a)
# print(a.sum(axis=0)) # axis=0, 행을 기준으로 각 행의 동일한 인덱스 요소를 그룹화
# print(a.sum(axis=1)) # axis=1, 열을 기준으로 각 열의 요소를 그룹화
#
# a = np.arange(1,10)
# print(a)
# b = np.arange(9,0, -1)
# print(b)
# print(np.dot(a,b)) #각 요소끼리 곱한 후 총합
#
#
# a = np.arange(1,5).reshape(2,2)
# print(a)
# b = np.arange(9,5, -1).reshape(2,2)
# print(b)
# print(np.dot(a,b)) #행렬곱셈
#
