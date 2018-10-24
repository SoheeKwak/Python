import numpy as np
import tensorflow as tf
tf.set_random_seed(777)


trees = np.loadtxt('trees.csv', unpack=True, skiprows=1, delimiter=',')
print(trees.shape)  # (3.31)
x1_data = trees[0]  # [둘레]
x2_data = trees[1]  # [높이]
y_data = trees[-1]  # [볼륨]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
w1 = tf.Variable(tf.random_uniform([1], -1, 1), name='weight1')
w2 = tf.Variable(tf.random_uniform([1], -1, 1), name='weight2')
y = tf.placeholder(tf.float32)
b = tf.Variable(tf.random_uniform([1], -1, 1), name='bias')

hf = x1 * w1 + x2 * w2 + b

cost = tf.reduce_mean(tf.square(hf - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00015)
train = optimizer.minimize(cost)

# 세션실행#
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 학습#
for step in range(50):
    cv, hv, _ = sess.run([cost, hf, train], feed_dict={x1: x1_data, x2: x2_data, y: y_data})
    if step % 10 == 0:
        print(step, "비용:", cv, "\n예측:\n", hv)

# 둘레:13, 높이:90, 볼륨?예측
print("둘레:13, 높이:90일때 예상되는 값:", sess.run(hf, feed_dict={x1:[13], x2:[90]}))


