# Logistic Classification
import tensorflow as tf
import numpy as np
      #3행 6열
xx = [[1,1,1,1,1,1], #x1
      [2,3,3,5,7,2], #x2
      [1,2,5,5,5,5,]] #x3
yy = np.array([0,0,0,1,1,1])

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_uniform([1,3],-1,1))

z = tf.matmul(w,x) #(1,3)*(3,6)=>(1,6)
hf = tf.nn.sigmoid(z) #또는 hf = 1/(1+tf.exp(-z)), 또는 hf = tf.div(1, 1+tf.exp(-z))
cost = -tf.reduce_mean(y*tf.log(hf)+(1-y)*tf.log(1-hf))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(cost)

for i in range(2001):
    sess.run([train], feed_dict={x:xx, y:yy})
    if i % 20 ==0 :
        print(i, sess.run(cost, feed_dict={x:xx, y:yy}))
print("="*50)

xx=[[1,1],
    [3,7],
    [8,2]]
print(sess.run(hf, feed_dict={x:xx}))

y_hat = sess.run(hf, feed_dict={x:xx})
print(y_hat > 0.5)
print(sess.run(w))

import math
def sigmoid(z):
    return 1/(1+math.e**-z)
ww = sess.run(w)
z = np.dot(ww,xx)

print(sigmoid(z))

