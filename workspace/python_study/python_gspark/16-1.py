import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

num = np.array(['3.14','-2.7','30'],dtype=np.string_)
num = num.astype(float).astype(int) #문자를 정수로 바꿀 시 먼저, float로 바꾼 후 int로 전환
print(num)

arr = np.arange(32).reshape((8,4))
print(arr)
print(arr[[1,5,7,2],[0,3,1,2]])
print(arr[[1,5,7,2]][:,[0,3,1,2]]) #1,5,7,2번 행을 먼저 추출한 후, 전체 행에 대해 0,3,1,2열 순대로 추출
         # <- 행 ->  <-   열  ->

position = 0
walk = []
import random
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1 #random.randint(0,1)=> 0 또는 1이 1000번 반복될텐데 1이 나옴 참이므로 1이 되고, 0이 나옴 거짓이므로 -1
    position+=step
    walk.append(position)
print("position:",position)
print("walk:",walk)
print(min(walk))
print(max(walk))

print(np.abs(walk)) #np.abs:절대값
