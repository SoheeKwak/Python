import tensorflow as tf

a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)
add = tf.add(a,b)
# a에 3, b에 4를 전달한 후 합을 출력하는 코드 작성
sess = tf.Session()
print(sess.run(add, feed_dict={a:3, b:4}))
######################################### 또는
a = tf.Variable(3)
b = tf.Variable(4)
add = tf.add(a,b)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(add))

"""placeholder 사용 구구단 출력
2단 출력
2 * 1 = 2
2 * 2 = 4
"""
def show99(dan):
    left = tf.placeholder(tf.int32)
    right = tf.placeholder(tf.int32)
    op = tf.multiply(left,right)
    sess = tf.Session()
    for i in range(1,10):
        res = sess.run(op, feed_dict={left:dan, right:i})
        print('{} * {} = {}'.format(dan, i, res))

show99(2)

