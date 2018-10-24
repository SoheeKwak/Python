import tensorflow as tf
tf.set_random_seed(999)
x=[1,2,3]
y=[1,2,3]
w = tf.placeholder(tf.float32)
hf = x*w #b는 생략
cost = tf.reduce_mean(tf.square(hf-y))
sess = tf.Session()

#시각화 하는 데 사용되는 리스트
w_history=[]
cost_history =[]

for i in range(-40, 50):
    cw=i*0.1 #-4, -3.9, ..., 4.8, 4.9
    cur_cost = sess.run(cost,feed_dict={w:cw})
    w_history.append(cw)
    cost_history.append(cur_cost)

import matplotlib.pyplot as plt
plt.plot(w_history, cost_history)
plt.show()