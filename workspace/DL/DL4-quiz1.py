## Classification of Diabetes

import tensorflow as tf
import numpy as np
tf.set_random_seed(777)

xy = np.loadtxt('diabetes.csv', delimiter=",", dtype=np.float32)
print(xy)
x_data = xy[:,:-1]
print(x_data.shape) #(759, 8)
y_data = xy[:,[-1]]
print(y_data.shape) #(759, 1)

#training data
x_train = x_data[:601,:]
y_train = y_data[:601,:]
#test data
x_test = x_data[601:,:]
y_test = y_data[601:,:]

x = tf.placeholder(tf.float32, shape=[None,8])
y = tf.placeholder(tf.float32, shape=[None,1])

w = tf.Variable(tf.random_normal([8,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hf = tf.sigmoid(tf.matmul(x,w)+b)
cost = -tf.reduce_mean(y*tf.log(hf)+(1-y)*tf.log(1-hf))
train = tf.train.GradientDescentOptimizer(0.3).minimize(cost)


## Launch graph
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    cv, hv, _ = sess.run([cost, hf, train], feed_dict={x:x_train, y:y_train})
    if step%200==0:
        print(step, cv)
cv, wv, bv = sess.run([cost,w,b], feed_dict={x:x_train, y:y_train})
print("Cost:", cv, "Weight:", wv, "Bias:", bv)


## Accuracy computation
predicted = tf.cast(hf > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,y),dtype=tf.float32))
hv, pv, av = sess.run([hf, predicted, accuracy], feed_dict={x:x_test, y:y_test})
print("\n예측값:",hv, "\n예측값(0/1):",pv, "\n정확도:",av)






