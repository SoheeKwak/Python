import tensorflow as tf
tf.set_random_seed(999)

x_data = [1,2,3]
y_data = [1,2,3]
w = tf.Variable(tf.random_normal([1]))
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
hf = x*w

cost = tf.reduce_mean(tf.square(hf-y))
lr = 0.1
gradient = tf.reduce_mean((w*x-y)*x)
descent = w-lr*gradient
update = w.assign(descent) # update를 실행하면 w에 대한 갱신이 수행됨
#위 4줄 코드는 의미상 아래의 코드와 동일
# tf.train.GradientDescentOptimizer(0.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(21):
    sess.run(update, feed_dict={x:x_data, y:y_data})
#위 문장을 수행함으로써 w가 갱신됨
    print(step, sess.run(cost,feed_dict={x:x_data, y:y_data}), sess.run(w))