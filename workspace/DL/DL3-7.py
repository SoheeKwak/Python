import tensorflow as tf
tf.set_random_seed(777)

x_data =  [[280, 310, 270],
           [310, 300, 325],
           [250, 225, 205],
           [270, 267, 290],
           [277, 307, 300]]

y_data =  [[299],
           [327],
           [240],
           [270],
           [290]] #수능점수

x = tf.placeholder(tf.float32, shape=[None,3]) #3회 모의고사는 고정, 학생은 늘어날 수 있음을 감안
y =  tf.placeholder(tf.float32, shape=[None,1]) #1회 수능 고정, 학생은 x와 같은 수의 데이타

w = tf.Variable(tf.random_normal([3,1]), name='w1')
b  = tf.Variable(tf.random_normal([1]), name='bias')

hf = tf.matmul(x,w) + b  #[None,3]*[3,1]=>[None,1]
cost = tf.reduce_mean(tf.square(hf-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-6)
train = optimizer.minimize(cost)

#세션실행#
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#학습#
for step in range(10001):
    cv, hv, _ = sess.run([cost, hf, train], feed_dict={x:x_data,y:y_data})
    if step%10==0:
        print(step, "비용:", cv, "\n예측:\n", hv)

