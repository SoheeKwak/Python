import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2],[3,4],[5,6]])
print(A.shape) #(3, 2)

# 행렬의 내적
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))

A = np.array([[1,2,3],[4,5,6]]) #2*3
B = np.array([[1,2],[3,4],[5,6]])#3*2
print(np.dot(A,B)) #2*2

# A가 2차원,B가 1차원일때도 차원의 원소 수를 일치 (3*2) (2,) = 3
A = np.array([[1,2],[3,4],[5,6]])#(3*2)
B = np.array([7,8]) #(2,)
print(np.dot(A,B)) #(3,)


x = np.array([1,2]) #(2,)
w = np.array([[1,3,5],[2,4,6]]) #(2,3) 총 6개의 가중치를 갱신해 감
y = np.dot(x,w) #(3,)
print(y)


# Neural Network:forward propagation
def sigmoid(x):
    return  1/(1+np.exp(-x))
X = np.array([1.0, 0.5])
W1 = np.array([[0.1,0.3,0.5], [0.2,0.4,0.6]])
b1 = np.array([0.1,0.2,0.3])
A1 = np.dot(X,W1)+b1
Z1 = sigmoid(A1)
print(A1)
print(Z1)

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
b2 = np.array([0.1,0.2])
print(Z1.shape, W2.shape, b2.shape)

A2 = np.dot(Z1,W2)+b2   #Z1이 바로 이전 노드(계층)의 출력값=A1
Z2 = sigmoid(A2)

W3 = np.array([[0.1,0.3],[0.2,0.4]])
b3 = np.array([0.1,0.2])

A3 = np.dot(Z2, W3)+b3
print(A3)