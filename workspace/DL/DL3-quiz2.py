import numpy as np
import tensorflow as tf
tf.set_random_seed(777)

xy = np.loadtxt('score.csv', delimiter=",", dtype=np.float32)
x_data = xy[:, 0:-1]
print(x_data)
y_data=xy[:, [-1]]
print(y_data)

x = tf.placeholder(tf.float32, shape=[None,3])
y =  tf.placeholder(tf.float32, shape=[None,1])

w = tf.Variable(tf.random_normal([3,1]), name='weight')
b  = tf.Variable(tf.random_normal([1]), name='bias')

hf = tf.matmul(x,w) + b  #[None,3]*[3,1]=>[None,1]
cost = tf.reduce_mean(tf.square(hf-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=5e-5)
train = optimizer.minimize(cost)

#세션실행#
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#학습#
for step in range(10001):
    cv, hv, _ = sess.run([cost, hf, train], feed_dict={x:x_data,y:y_data})
    if step%100==0:
        print(step, cv)

print("============모델==================")
cv, wv, bv = sess.run([cost,w,b], feed_dict={x:x_data, y:y_data})
print("비용:", cv, "가중치:", wv, "편향:", bv)

#테스트#
predict = [[100, 70, 102],
          [60, 70, 100],
        [80, 90, 95]]
model_hf = tf.matmul(x,wv) + bv
print("============모델로 테스트한 값==================")
print("학생1, 2, 3의 예측 수능점수:", sess.run(model_hf,feed_dict={x:predict}))

