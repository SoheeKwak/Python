import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
np.random.seed(20181105)
tf.set_random_seed(20181105)

#load data
mnist = input_data.read_data_sets('tmp/data/',one_hot=True)

#28*28*1(흑백) 이미지에 5*5*1 필터를 적용 => 24*24*1
num_filters1 = 32
x = tf.placeholder(tf.float32, [None,784]) #28*28*1
x_image = tf.reshape(x, [-1, 28, 28, 1]) #-1:None과 같은 의미, 즉, 28*28*1의 행렬이 무한개(-1)
#연산의 편의를 위해 784(1차원 벡터)->2차원 28*28*1행렬 reshape
W_conv1 = tf.Variable(tf.random_normal([5,5,1, num_filters1])) #num_filters1:필터의 갯수, W_conv1의 차원(shape):[5,5,1,32], 즉 W가 5*5*1*32개

# 필터에 입력 이미지 적용
h_conv1 = tf.nn.conv2d(x_image, W_conv1, strides=[1,1,1,1], padding="SAME") #strides:통상적으로 맨앞과 뒤는 1씩 준다. 중간에 두값이 실질적인 가로/세로 방향 이동 칸 수
#28*28 = W(32*32) * x(5*5)  ->패딩:필터를 적용하면 추출된 특징 행렬은 원이미지보다 크기가 작아짐. 계속 적용 하면 특징이 유실되는 문제 발생. 따라서 원본데이터와 크기만 같게하는 패딩 적용

#필터 적용이 끝나면 활성화 함수 적용(CNN-Relu함수)
b_conv1 = tf.Variable(tf.constant(0.1, shape=[num_filters1])) # b는 필터 갯수만큼 필요
h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)

#Pooling:max pooling 적용->추출된 특징 모두를 사용해서 특징을 판단하지 않고, 일부 특징만 갖고 특징을 판단.
h_pool1 = tf.nn.max_pool(h_conv1_cutoff, ksize=[1,2,2,1], strides=[1,2,2,1],padding="SAME")#ksize:풀링 시 필터(kernel)의 크기(2*2)의 크기로 묶어서 풀링, strides:오른쪽으로 2ㅋㄴ, 아래쪽으로 2칸

#행렬의 차원 변환

#두번째 convolution 계층
num_filters2 = 64
W_conv2 = tf.Variable(tf.random_normal([5,5,num_filters1, num_filters2]))#[5,5,32,64]필터의 크기(5*5), 입력되는값32개(이전conv1출력값 필터갯수), 총64개 필터가 적용됨

h_conv2 = tf.nn.conv2d(h_pool1, W_conv2, strides=[1,1,1,1], padding="SAME")
b_conv2 = tf.Variable(tf.constant(0.1, shape=[num_filters2]))
h_conv2_cutoff = tf.nn.relu(h_conv2 + b_conv2)
h_pool2 = tf.nn.max_pool(h_conv2_cutoff, ksize=[1,2,2,1], strides=[1,2,2,1],padding="SAME")
"""
28*28(첫번째 풀링2*2)->14*14->(두번째 풀링2*2)->7*7
결국 7*7크기의 행렬이 64개 나옴
fully connected layer:64개의 입력으로부터 10개의 숫자로 분류
두번째 convolution에서 특징을 뽑아냈으면 이 특징으로 0~9까지의 숫자를 판별하기 위한 fully connected layer구성"""

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*num_filters2]) #입력된 64개의 7*7행렬을 1차원 행렬로 변환
num_units1 = 7*7*num_filters2
num_units2 = 1024

W2 = tf.Variable(tf.random_normal([7*7*num_filters2, num_units2]))
b2 = tf.Variable(tf.constant(0.1, shape=[num_units2]))
hidden2 = tf.nn.relu(tf.matmul(h_pool2_flat, W2)+b2)

keep_prob = tf.placeholder(tf.float32)
hidden2_drop = tf.nn.dropout(hidden2, keep_prob)

W0 = tf.Variable(tf.zeros([num_units2,10]))
b0 = tf.Variable(tf.zeros([10]))
k = tf.matmul(hidden2_drop, W0) +b0
p = tf.nn.softmax(k)

# 비용함수 정의
#cost:cross-entropy 함수 적용
t = tf.placeholder(tf.float32, [None, 10])
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=k, labels=t)) # t:실제값
train_step = tf.train.AdamOptimizer(0.0001).minimize(loss)
correct_prediction = tf.equal(tf.argmax(p,1), tf.argmax(t,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
saver = tf.train.Saver()

###학습 수행##
i = 0
for _ in range(10000):
    i +=1
    batch_xs, batch_ts = mnist.train.next_batch(50)
    sess.run(train_step, feed_dict={x:batch_xs, t:batch_ts, keep_prob:0.5})#dropout을 50%로 고정(7*7*64)*1024로 연결된 네트워크 중 50%를 끊어줌
    if i%500==0: #25000(50*500)개 트레이닝 후 처음 출력
        loss_vals, acc_vals = [],[]
        #학습비용, 정확도
        for c in range(4): #test_label:1만개
            start = int(len(mnist.test.labels)/4* c) #c=0일때:0, c=1:2500..5000..
            end = int(len(mnist.test.labels)/4* (c+1)) #c=0일때:2500, c=1:5000...7500
            loss_val, acc_val = sess.run([loss, accuracy],feed_dict={x:mnist.test.images[start:end], #[start:end]0:2500, 2500:5000, 5000:7500, 7500:10000 4회에 걸쳐
                                                                     t:mnist.test.labels[start:end],
                                                                     keep_prob:1.0})
            loss_vals.append(loss_val)
            acc_vals.append(acc_val)
            loss_val = np.sum(loss_vals)
            acc_val = np.mean(acc_vals)

            print("Step:%d, Loss:%f, Accuracy:%f"%(i, loss_val, acc_val))
saver.save(sess,'cnn_session')
sess.close()


