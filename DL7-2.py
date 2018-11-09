import tensorflow as tf
import csv
import numpy as np
tf.set_random_seed(777)

read = open("iris.csv", "r", encoding="utf-8")
print(read)
csvread = csv.reader(read)
print(csvread)
title = next(csvread) #첫번째줄 skip, 호출할 때마다 추가로 다음줄이 skip
print(title)
xdata = []
ydata = []

index = ['setosa','versicolor','virginica']
for row in csvread:
    data = []
    sepal_length = float(row[1])
    sepal_width = float(row[2])
    petal_length = float(row[3])
    petal_width = float(row[4])
    data=[sepal_length, sepal_width, petal_length,petal_width]
    xdata.append(data)

    for i in range(3):
        if row[5]==index[i]:
            ydata.append([i])
print(xdata)
print(ydata)

x = tf.placeholder(tf.float32, shape=[None,4])
y = tf.placeholder(tf.int32, shape=[None,1])

w = tf.Variable(tf.random_normal([4,3]))
b = tf.Variable(tf.random_normal([3]))

nb_classes = 3
y_one_hot = tf.one_hot(y, nb_classes) # [[0],[2]]=>[[[100]],[[001]]]
y_one_hot = tf.reshape(y_one_hot, [-1, nb_classes]) #[[[100]],[[001]]]->[[100]],[[001]]

logit = tf.matmul(x,w)+b
hf = tf.nn.softmax(logit)

costi = tf.nn.softmax_cross_entropy_with_logits(logits=logit, labels=y_one_hot)
cost = tf.reduce_mean(costi)

prediction = tf.argmax(hf,1)
correct_prediction = tf.equal(prediction, tf.argmax(y_one_hot,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype=tf.float32))
train = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cv, av, _ = sess.run([cost, accuracy, train],feed_dict={x:xdata,y:ydata})

    if step%20==0:
        print("cost:",cv, "acc:",av)

#True prediction: 1 True Y:1
pred = sess.run(prediction, feed_dict={x:xdata})
# [[100]],[[001]] -> flatten(1차원으로 변경)->[100, 001,...]
ydata = np.array(ydata, dtype=np.int32) #flatten함수는 넘파이에 있음. 따라서 ydata의 구조를 리스트->array로 변경
for p, y in zip(pred, ydata.flatten()):
    print("{} prediction:{} True Y:{}".format(p==y, p, y))
