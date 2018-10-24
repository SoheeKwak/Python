# linear regression
import tensorflow as tf
tf.set_random_seed(777)

"""
data-set: trainig(7)/test(3)
ex)data 100개: 트레이닝70개, 테스트30개
"""
#########그래프 정의############
x_train = [1,2,3]
y_train = [1,2,3]
# hx = w*x + b (여기선 트레이닝 횟수가 더해지면서 w는 1에, b는 0에 가까워질 것임)
w = tf.Variable(tf.random_normal([1]))  #정규화분포에서 임의의 난수 1개
b = tf.Variable(tf.random_normal([1]))

hf = w * x_train + b

cost = tf.reduce_mean(tf.square(hf - y_train))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

##########그래프 실행########
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train)
    if step%20==0:
        print(step, sess.run(cost), sess.run(w), sess.run(b))