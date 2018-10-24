import numpy as np
import tensorflow as tf
tf.set_random_seed(777)

xy = np.loadtxt('stock.csv', skiprows=1,delimiter=",", dtype=np.float32)
x_data = xy[:, 0:3]  # Open,High,Low 추출
y_data=xy[:, [-1]] # Close 추출

# Training Data: 1000번째 데이터까지 추출
x_train_data = x_data[:999]
y_train_data = y_data[:999]

# Test Data: 1001번째 데이터부터 추출
x_test_data = x_data[999:]
y_test_data = y_data[999:]

x = tf.placeholder(tf.float32, shape=[None,3])
y =  tf.placeholder(tf.float32, shape=[None,1])

w = tf.Variable(tf.random_normal([3,1]), name='weight')
b  = tf.Variable(tf.random_normal([1]), name='bias')

hf = tf.matmul(x,w) + b  #[None,3]*[3,1]=>[None,1]
cost = tf.reduce_mean(tf.square(hf-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=6e-7)
train = optimizer.minimize(cost)

#세션실행#
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#학습#
for step in range(10001):
    sess.run([train], feed_dict={x:x_train_data, y:y_train_data})
    if step%100==0:
        print(step, sess.run(cost, feed_dict={x: x_train_data, y:y_train_data}))
print("============모델==================")
cv, wv, bv = sess.run([cost,w,b], feed_dict={x:x_train_data, y:y_train_data})
print("비용:", cv, "가중치:", wv, "편향:", bv)


#테스트#
model_hf = tf.matmul(x,wv) + bv
print("============모델로 테스트한 값==================")
print(sess.run(model_hf,feed_dict={x:x_test_data, y:y_test_data}))


