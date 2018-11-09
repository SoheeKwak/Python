import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/",one_hot=True)

## 신경망 모델 구성
x = tf.placeholder(tf.float32, [None, 28*28])
y = tf.placeholder(tf.float32, [None, 10])
w1 = tf.Variable(tf.random_normal([28*28, 256],stddev=0.01)) # w1:입력계층과 1번째 히든계층 사이의 가중치, 256은 임의로 준 것(신경망의 은닉계층hidden layer설계자의 의도에 따라 달라질 수 있음
L1 = tf.nn.relu(tf.matmul(x,w1))

w2 = tf.Variable(tf.random_normal([256, 256],stddev=0.01)) #stddev:표준편차
L2 = tf.nn.relu(tf.matmul(L1,w2)) #신경망 구성 시 계속 시그모이드 함수 같은 것을 쓰면 출력값이 0~1사이므로 계층이 깉어질수록 출력값이 0에 가까워짐. 즉 w가 0에 가까워지므로 이를 피하기 위해 계층마다 그대로 보내주는 relu함수를 씀

w3 = tf.Variable(tf.random_normal([256, 10],stddev=0.01))
model = tf.matmul(L2,w3)   #마지막 모델만 렐루 함수가 아닌 시그모이드 등의 함수를 적용.

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)

######## 신경망 모델 학습 ########
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

batch_size = 100
total_batch = int(mnist.train.num_examples/batch_size)
for epoch in range(20):
    total_cost = 0
    for i in range(total_batch): #600번
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)#batch_xs, batch_ys각 shape (100,28*28), (100,10 one hot encoding)
        _, cv = sess.run([optimizer, cost], feed_dict={x:batch_xs, y:batch_ys})
        total_cost +=cv
    print("epoch:","%5d"%(epoch+1),
          "avg cost:","{:.10f}".format(total_cost/total_batch))
    is_correct = tf.equal(tf.argmax(model,1), tf.argmax(y,1))
    accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
    print("정확도:",sess.run(accuracy,feed_dict={x:mnist.test.images, y:mnist.test.labels}))