# Mushroom_ Logistic Regression
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

Xy=pd.read_csv("mushroom.txt", header=None)
# print(Xy)
le = LabelEncoder() #Encoding: string->integer
for col in Xy.columns:
    Xy[col] = le.fit_transform(Xy[col])
    # print(Xy[col] )

X = Xy.iloc[:, 1:].values
y = Xy.iloc[:,[0]].values
# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=58)
print(X_train.shape, y_train.shape) #(5686, 22) (5686, 1)

X = tf.placeholder(tf.float32, shape=[None,22])
y = tf.placeholder(tf.float32, shape=[None,1])
W = tf.Variable(tf.random_normal([22,1]),name='weight')
b = tf.Variable(tf.random_normal([1]),name='bias')

hf = tf.sigmoid(tf.matmul(X, W)+b)
cost = -tf.reduce_mean(y*tf.log(hf)+(1-y)*tf.log(1-hf))
optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

predicted = tf.cast(hf >0.5, dtype =tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cv,yhat, _ = sess.run([cost, hf, optimizer], feed_dict={X:X_train, y:y_train})
        if step%1000==0:
            print(step, cv, yhat)
        pred, acc = sess.run([predicted, accuracy], feed_dict={X:X_test, y:y_test})

for p, y in zip(pred, y_test):
    print("{} prediction:{} True Y:{}".format(p==y,p,y))
print("Accuracy: ", acc)
