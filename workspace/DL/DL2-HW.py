import numpy as np
import tensorflow as tf
tf.set_random_seed(777)

###속도가 30일때와 50일때의 제동거리를 예측하시오.

cars = np.loadtxt('cars.csv', delimiter=",")
xx, yy = [],[]
for speed, distance in cars:
    xx.append(speed)
    yy.append(distance)
print(xx)
print(yy)

#########그래프 정의############
w = tf.Variable(tf.random_normal([1]))  #정규화분포에서 임의의 난수 1개
b = tf.Variable(tf.random_normal([1]))

x = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])
hf = w * x + b

cost = tf.reduce_mean(tf.square(hf - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.003)
train = optimizer.minimize(cost)

##########그래프 실행########
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train, feed_dict={x:xx, y:yy})
    if step%20==0:
        print(step, sess.run(cost, feed_dict={x:xx, y:yy}))

print("==========모델==================")
cv, wv, bv = sess.run([cost,w,b], feed_dict={x:xx, y:yy})
print("비용:", cv, "가중치:", wv, "편향:", bv)

#######예측해보기###########
# x=30, x=50 일때 예측 제동거리 ???

print("30일때 예상되는 값:", sess.run(hf, feed_dict={x:[30]}))
print("50일때 예상되는 값:", sess.run(hf, feed_dict={x:[50]}))


