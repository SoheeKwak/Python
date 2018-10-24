import numpy as np
import tensorflow as tf

xy = np.loadtxt('xy.txt', skiprows=1) #1행이 문자라서 읽히지 않음. 따라서 skip
print(xy)
print(xy.shape)
print(type(xy))

xxy = np.loadtxt('xxy.csv', delimiter=",") # 자료 첫번째줄이 위와 달리 '#'표시가 있어서 무시하고 자동하고 skip이 됨. but, 그 다음줄부터 콤마(,)가 있어서 안읽히므로 delimiter
print(xxy)
xxy2 = np.loadtxt('xxy.csv', delimiter=",", unpack=True) # unpack:행열이 바뀜
print(xxy2)
print("="*50)

#############################################
cars = np.loadtxt('cars.csv', delimiter=",")
print(cars)
print(cars.shape)
xx, yy = [],[]
print(cars[1])
print(cars.shape[0]) #총50개
######################################3
# for i in range(cars.shape[0]):
for i in range(len(cars)):
    item = cars[i]
    xx.append(item[0]) #스피드 speed
    yy.append(item[1])  # 제동거리 distance
print(xx)
print("="*50)
print(yy)
##################################
for row in cars:
    xx.append(row[0])
    yy.append(row[1])
######################################
for speed, distance in cars:
    xx.append(speed)
    yy.append(distance)

cars = np.loadtxt('cars.csv', delimiter=",", unpack=True)
print(cars.shape) #(2, 50)
print(cars)
x=cars[0] #스피드
y=cars[1] #제동거리

cars = cars.transpose() #unpack에서 다시 행렬이 바뀜
print(cars.shape)