import numpy as np
import matplotlib.pyplot as plt

def step_function(x): #계단 함수:비선형함수, 0~1사이 (이 두가지가 sigmoid함수와 공통점)
    return np.array(x > 0, dtype=np.int)
X = np.arange(-5.0, 5.0, 0.1)
y = step_function(X)
print(y)
plt.plot(X,y)
plt.ylim(-0.1, 1.1)
plt.show()

def relu(x):
    return np.maximum(0,x) #relu함수:두 값중 최대값을 출력(if x<0, 0출력, else,x 그대로 출력)

X = np.arange(-5.0, 5.0, 0.1)
y = relu(X)
print(y)
plt.plot(X,y)
plt.ylim(-1.0, 5.5)
plt.show()
