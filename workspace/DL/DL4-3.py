# Logistic Classification
import tensorflow as tf
import numpy as np


tf.set_random_seed(777)
xdata = [[1,2], #x1=2일때 아래 y=0
         [2,3],  #x2=3일때 아래 y=0
         [3,1],
         [4,3],
         [5,3],
         [6,2]]

ydata = [[0],
         [0],
         [0],
         [1],
         [1],
         [1]]
x= tf.placeholder(tf.float32, shape=[None, 2])
y= tf.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.random_normal([2,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hf = tf.sigmoid(tf.matmul(x,w)+b)
cost = -tf.reduce_mean(y*tf.log(hf)+(1-y)*tf.log(1-hf))

train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

##정확도 계산
predicted = tf.cast(hf > 0.5, dtype=tf.float32) #cast:임계치 0.5보다 크면 1, 작으면 0
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y),dtype=tf.float32)) #equal:같으면 True, 다르면 False, 이것을 다시 cast하면 true=1, false=0, 이것을 reduce_mean:전체합계의 평균(즉 True=1값들만 더한것/결과데이터갯수)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cv, _ = sess.run([cost, train], feed_dict={x:xdata, y:ydata})
        if step % 200==0:
            print(step, cv)
    hfv, pv, av = sess.run([hf, predicted, accuracy], feed_dict={x:xdata, y:ydata})
    print("\n예측값:",hfv, "\n예측값(0/1):",pv, "\n정확도:",av)
