import tensorflow as tf
import random
import matplotlib.pyplot as plt
tf.set_random_seed(777)

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#28*28(784개)의 픽셀로 구성된 숫자 이미지 데이터
#6만 개-트레이닝 데이터셋
#1만 개-테스트 데이터셋 다운로드
nb_classes = 10 #0~9
x = tf.placeholder(tf.float32, [None, 28*28])
y = tf.placeholder(tf.float32, [None, nb_classes]) #10개 숫자 종류별 확률
w = tf.Variable(tf.random_normal([28*28, nb_classes]))
b = tf.Variable(tf.random_normal([nb_classes]))

hf = tf.nn.softmax(tf.matmul(x,w)+b)
cost = tf.reduce_mean(tf.reduce_sum(y*-tf.log(hf), axis=1))
optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(cost)
is_correct = tf.equal(tf.argmax(hf,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

training_epochs = 15
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples/batch_size) #mnist.train.num_examples:트레이닝용 데이터의 갯수(6만개)/배치100개씩 읽어줌, 즉, 600번 읽어줌
        for i in range(total_batch): #600번
            batch_xs, batch_ys = mnist.train.next_batch(batch_size) #트레이닝용 데이터(x,y)를 100개씩 읽어내려감
            c, _ = sess.run([cost, optimizer], feed_dict={x:batch_xs, y:batch_ys})
            avg_cost += c/total_batch #평균 cost 즉, 각 100개씩 읽어서 나온 cost의 총합/total_batch
        print('epoch:','%4d'%(epoch+1),'cost:','{:.9f}'.format(avg_cost))
    print("학습이 완료됨(모델 완성)")

    print("accuracy:", sess.run([accuracy], feed_dict={x:mnist.test.images, y:mnist.test.labels})) #mnist.test.images:테스트용 x데이터 1만개, labels:테스트용 라벨 y실제값(정답)1만개

    r = random.randint(0, mnist.test.num_examples-1) #1만개의 테스트용 이미지 중 1개 숫자를 랜덤으로 추출
    print("Label:", sess.run(tf.argmax(mnist.test.labels[r:r+1],1))) #테스트용 데이터의 r번째 y값의 최대값 인덱스
    print("Prediction:", sess.run(tf.argmax(hf,1), feed_dict={x:mnist.test.images[r:r+1]})) #테스트용 이미지 r번째 x요소 (예측이므로 y실제값은 알려주지 않음)

    plt.imshow(mnist.test.images[r:r+1].reshape(28,28))
    plt.show()