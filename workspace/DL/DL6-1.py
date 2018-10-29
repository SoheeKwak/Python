import numpy as np
import tensorflow as tf

xy = np.loadtxt("softmax.txt", dtype=np.float32, encoding='utf-8')
print(xy)
xx = xy[:,:3] #입력
y = xy[:,3:] #출력
print(xx) #(8,3)
print(y)#(8,3)

x = tf.placeholder(tf.float32)
w = tf.Variable(tf.zeros([3,3]))

z = tf.matmul(x,w)
hf = tf.nn.softmax(z) #z값이 확률로 출력

cost = tf.reduce_mean(tf.reduce_sum(y* -tf.log(hf), axis=1)) #reduce_sum:element multiply로 각 열별(axis=1)로 더해줌
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(2001):
    sess.run(train, feed_dict={x:xx})
    if i % 20 == 0:
        print(sess.run(cost, feed_dict={x:xx})) #y=y이므로 굳이 feed_dict할 필요 없음
# x가 [1, 11, 7], [1, 3, 4]일때 y(성적)예측
yhat = sess.run(hf, feed_dict={x:[[1, 11, 7], [1, 3, 4]]})
print(yhat)
grades = ['A','B','C']
yhat2 = sess.run(tf.argmax(yhat,axis=1))
print(yhat2) #[0,2] 각 x데이터에 대한 y값 중 최대값의 인덱스
print(grades[yhat2[0]], grades[yhat2[1]]) # A C
# #########################################
grades = np.array(['A','B','C'])
print(grades[yhat2]) #['A' 'C']




# ################################################################
import math
def softmax(): #softmax function
    aa = math.e**2.0
    bb = math.e**1.0
    cc = math.e**0.1
    base = aa+bb+cc
    print(aa/base) #0.7
    print(bb/base) #0.2
    print(cc/base) #0.1
                #sum: 1 (확률)
softmax()

