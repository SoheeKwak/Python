import numpy as np

a = np.array([1,3,5])
print(a)
print(type(a))

b = np.arange(7)
print(b)
b+=1
print(b) # broadcasting
print(b<4)
print(b[b<4])

c = np.arange(3,7,0.1)
print(c)

# d = np.arange(15).reshape(3,5)  # reshape 3행5열
# print(d)
# print(d.shape)

d2 = np.arange(24).reshape(2,3,4) # 2면 3행 4열 (3차원)
print(d2)
print(d2.shape)

d3 = np.arange(48).reshape(2,3,4,2) # 3면 4행 2열 (4차원)
print(d3)
print(d3.shape)

d = np.arange(15).reshape(3,5)
print(d)
print(d.shape)
print(d+1)
print(d[d>5])
print(d)
print(d[0])
print(d[-1]) #-1번째, 즉 마지막 행
print(d[0][0]) #0번째 행의 0번째
print(d[0,0])
print(d[-1][-1])
print(d[-1,-1])

print(d[::-1]) #마지막 행부터 거꾸로 출력
print(d[::-1][::-1])
print(d[::-1, ::-1]) #대괄호 안에 콤마로 있으면 행과 열로 구분, 마지막 행부터 거꾸로 읽은 후 다시 마지막 열부터 출력


print(d[1:3, 2:4]) #1,2번째 행에서 2,3번째 열에 해당하는 값을 출력
print(d.sum())
print(d)
print(d.sum(axis=0)) #축 (열을 더한 값)
print(d.sum(axis=1)) # 행단위로 더함

