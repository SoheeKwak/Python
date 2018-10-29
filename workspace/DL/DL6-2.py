import numpy as np
import tensorflow as tf

def read_iris_softmax():
    iris = np.loadtxt('iris_softmax.csv',delimiter=',')
    print(iris.shape) #(150, 8)

    # 120개의 트레이닝 데이터셋 모델 작성
    train_set = np.vstack((iris[:40], iris[50:90], iris[100:140])) #각 iris종류별로 40개씩 추출해서 하나의 데이터로 합해줌(vstack). 만약 앞에서부터 [:121]로 추출하면 같은 종류만 120개 출력됨
    print(train_set)
    print(train_set.shape) #(120,8)의 모양을 갖는 매트릭스가 출력됨

    # 30개의 test데이터셋으로 검증
    test_set = np.vstack((iris[40:50], iris[90:100], iris[140:]))
    print(test_set.shape) #(30, 8)
    return train_set, test_set

train_set, test_set = read_iris_softmax()
xx = train_set[:, :-3]
print(xx.shape) #(120, 5)
y = train_set[:, -3:]
print(y.shape) #(120, 3)

x = tf.placeholder(tf.float32)
w = tf.Variable(tf.zeros([5,3]))

z = tf.matmul(x,w) #b생략
hf = tf.nn.softmax(z)
cost = tf.reduce_mean(tf.reduce_sum(y*-tf.log(hf), axis=1)) #tf.reduce_sum: y*-tf.log(hf)로 나온 값들의 합을 구해야 함

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(2001):
    sess.run(train, feed_dict={x:xx})
    if i%20==0:
        print(i, sess.run(cost, feed_dict={x:xx}))

######### test 데이터 셋을 이용한 모델 검증 ############
xx = test_set[:,:-3] #(30, 5)
y =  test_set[:, -3:] #(30, 3)

yhat = sess.run(hf, feed_dict={x:xx})
print(yhat)
yhat2 = sess.run(tf.argmax(yhat, axis=1))
print("예측값:", yhat2)

y2 = sess.run(tf.argmax(y,axis=1))
print("실제값:",y2)

equal = sess.run(tf.equal(yhat2,y2))
print(equal)

cast=sess.run(tf.cast(equal, tf.float32))
print(cast)

mean = sess.run(tf.reduce_mean(cast))
print(mean) #1.0:전체 일치

### 텐서플로우 대신 넘파이 활용 ######
yhat2 = np.argmax(yhat, axis=1)
print(yhat2)
y2 = np.argmax(y, axis=1)
print(y2)

equal= (yhat2==y2)
print(equal)

mean = np.mean(equal)
print(mean)