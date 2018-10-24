import tensorflow as tf

# w와 b에 대한 초기값을 부여한 상태에서 모델링
w=tf.Variable([.3], tf.float32)
b=tf.Variable([-.3], tf.float32)
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
lm=x*w+b
loss=tf.reduce_sum(tf.square(lm-y))

train=tf.train.GradientDescentOptimizer(0.01).minimize(loss)
x_train=[1,2,3,4]
y_train=[0,-1,-2,-3]

#트레이닝 횟수 1000번->모델생성
#생성된 모델의 w, b, loss출력
sess=tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    sess.run(train,feed_dict={x:x_train,y:y_train})

wv, bv, lossv = sess.run([w,b,loss],feed_dict={x:x_train, y:y_train})
print("w값:%s b값:%s loss값:%s" % (wv, bv, lossv))

