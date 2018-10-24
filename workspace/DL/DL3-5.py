import tensorflow as tf
# Multi-Variable regression
def not_used():
    x1 = [1,0,3,0,5]
    x2 = [0,2,0,4,0]
    y =  [1,2,3,4,5]
    #위 데이터는 instance가 5개, 입력변수는 2개 따라서 가중치도 2개가 되어야 함
    w1 = tf.Variable(tf.random_uniform[1], -1, 1) # -1에서 1사이의 난수 1개 생성
    w2 = tf.Variable(tf.random_uniform[1], -1, 1)
    b = tf.Variable(tf.random_uniform[1], -1, 1)

    hf = x1*w1 + x2*w2 + b
    cost = tf.reduce_mean((hf-y)**2)
    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(cost)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
    sess.close()


def not_used_2():
    x = [[1, 0, 3, 0, 5],
         [0, 2, 0, 4, 0]]
    y = [1, 2, 3, 4, 5]
    # 위 데이터는 instance가 5개, 입력변수는 2개 따라서 가중치도 2개가 되어야 함
    w = tf.Variable(tf.random_uniform[1, 2], -1, 1)  # [1, 2]: x(2행5열)에 따라 예측값이 1행5열이 돼야하므로 w도 1행2열이 돼야 함
    b = tf.Variable(tf.random_uniform[1], -1, 1)
    """
    (1,2) * (2,5) = (1,5)
      w   *   x   =  hf 
    """
    hf = tf.matmul(w,x) + b #matmul: 행렬간의 곱
    cost = tf.reduce_mean((hf - y) ** 2)
    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(cost)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
    sess.close()


import numpy as np
def not_used_3():
    trees = np.loadtxt('trees.csv', skiprows=1, delimiter=',')
    print(trees)
    x = [[1, 1, 1, 1, 1],
         [1, 0, 3, 0, 5],
         [0, 2, 0, 4, 0]]
    y = [1, 2, 3, 4, 5]
    # 위 데이터는 instance가 5개, 입력변수는 2개 따라서 가중치도 2개가 되어야 함
    w = tf.Variable(tf.random_uniform[1, 3], -1, 1)  # [1, 3]: x(3행5열)에 따라 예측값이 1행5열이 돼야하므로 w도 1행3열이 돼야 함
    b = tf.Variable(tf.random_uniform[1], -1, 1)
    """
    (1,3) * (3,5) = (1,5)
      w   *   x   =  hf 
    """
    hf = tf.matmul(w,x) + b   #matmul: 행렬간의 곱
    cost = tf.reduce_mean((hf - y) ** 2)
    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(cost)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
    sess.close()


not_used()
not_used_2()
not_used_3()