import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

td1 = tf.argmax([[5,1,4],
                [4,5,6]], axis=0) #2행 3열, argmax(axis=0)같은 열끼리 비교해서 더 큰값이 있는 행을 추출. 즉 열 내에서 최대값의 위치

td2 = tf.argmax([[5,1,4],
                [4,5,6]], axis=1) #행 내에서 최대값의 위치
sess = tf.Session()

print(sess.run(td1))
print(sess.run(td2))

###############################################################
x = np.arange(6).reshape(2,3)
k = tf.reduce_sum(x) #행렬의 전체 요소를 모두 더한 값
print(sess.run(k))
# resuce:차원이 축소됨
print(sess.run(tf.reduce_sum(x)))         #행렬의 전체 요소를 모두 더한 값
print(sess.run(tf.reduce_sum(x, axis=0))) #열 단위 합
print(sess.run(tf.reduce_sum(x, axis=1))) #행 단위 합

################################################################
# y:실제값,yhat:예측값 ->전달받아 cost를 리턴하는 함수
def costToYhat(y, yhat):
    cost = 0
    # cost: y-yhat의 제곱의 합의 평균
    for i in range(len(y)):
        cost +=(y[i]-yhat[i])**2
    return cost/len(y)

y = [1,2,3]
yhat = [2,4,6]
print(costToYhat(y,yhat))



