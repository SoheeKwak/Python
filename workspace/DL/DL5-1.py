import numpy as np
import  tensorflow as tf
tf.set_random_seed(777)

xy = np.loadtxt('diabetes.csv', delimiter=',',dtype=np.float32)
print(xy)
xdata = xy[:, 0:-1]
ydata = xy[:, [-1]]
print(xdata.shape, ydata.shape) #(759, 8) (759, 1)

x = tf.placeholder(tf.float32, shape=[None, 8])
y = tf.placeholder(tf.float32, shape=[None, 1])
w = tf.Variable(tf.random_normal([8,1]))
b = tf.Variable(tf.random_normal([1]))

hf = tf.sigmoid(tf.matmul(x,w)+b)
cost = -tf.reduce_mean(y*tf.log(hf)+(1-y)*tf.log(1-hf))
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
predicted = tf.cast(hf>0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cv, _ = sess.run([cost,train],feed_dict={x:xdata, y:ydata})
        if step%200==0:
            print(step, cv)
    hv, cv, av = sess.run([hf, predicted, accuracy], feed_dict={x:xdata, y:ydata})
    print("\n가설:",hv, "\n예측:",cv,"\n정확도:",av)

