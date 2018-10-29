import tensorflow as tf
import numpy as np
tf.set_random_seed(777)
        # x1,x2, x3,x4
x_data = [[1, 2, 1, 1],
          [2, 1, 3, 2],
          [3, 1, 3, 4],
          [4, 1, 5, 5],
          [1, 7, 5, 5],
          [1, 2, 5, 6],
          [1, 6, 6, 6],
          [1, 7, 7, 7]]
y_data = [[0, 0, 1],#2
          [0, 0, 1],#2
          [0, 0, 1],#2
          [0, 1, 0],#1
          [0, 1, 0],#1
          [0, 1, 0],#1
          [1, 0, 0],#0
          [1, 0, 0]]#0

""" 조건:
x값이 [[1,11,7,9],[1,3,4,3],[1,1,0,1]]일때 분류결과를 출력하시오.
x,y=플레이스홀더
클래스 개수=3
w,b=변수(랜덤값 초기화)
learning rate=0.1
트레이닝 횟수:2001
"""
x = tf.placeholder(tf.float32, shape=[None, 4])
y = tf.placeholder(tf.float32, shape=[None, 3])

w = tf.Variable(tf.random_normal([4,3]))
b = tf.Variable(tf.random_normal([3]))

z = tf.matmul(x,w)+b
hf = tf.nn.softmax(z)

cost = tf.reduce_mean(tf.reduce_sum(y*-tf.log(hf), axis=1))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(cost)

# 모델 생성
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(2001):
    sess.run(train, feed_dict={x:x_data, y:y_data})
    if i%20==0:
        print(sess.run(cost, feed_dict={x:x_data, y:y_data}))

# x값이 [[1,11,7,9],[1,3,4,3],[1,1,0,1]]일때 예측
yhat = sess.run(hf, feed_dict={x:[[1,11,7,9],[1,3,4,3],[1,1,0,1]]})
print(yhat)
yhat2 = sess.run(tf.argmax(yhat, axis=1))
print(yhat2)


