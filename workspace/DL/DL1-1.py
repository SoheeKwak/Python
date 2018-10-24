import tensorflow as tf

hello = tf.constant('hello')
# print(hello) #텐서에 대한 정보
sess = tf.Session() #Session이라는 객체를 sess라고 정의한다.
# print(sess)
print(sess.run(hello)) # 그래프 실행:b'hello', b:binary
print(str(sess.run(hello), encoding='utf-8'))

#############그래프 정의(build) ###################
a = tf.constant(5, dtype=tf.float32)  #a, b, c: constant(상수)
b = tf.constant(10, dtype=tf.float32)
c = tf.constant(2, dtype=tf.float32)
d = a*b + c    # node(연산):a에 b를 곱한 후 c를 더하는 연산을 d라는 노드로 정의한다.
# print(d) #여기선 d값이 안나옴, 밑에서 run시행해야 나옴
##그래프 실행(run) ##
sess = tf.Session()
res = sess.run(d) # d(노드)를 실행한 결과를 res(변수)에 저장하라.
print(res)
###############################

a = tf.constant(3) #3은 스칼라(0차 텐서)
print(a)
# sess= tf.Session()
# print(sess.run(a))
# sess.close() #세션 종료->메모리 자원 반환

with tf.Session() as sess: #sess라는 이름으로 세션객체를 만들어라. 위와 같은 표현이지만 with를 쓰면 구문을 빠져나올 시 자동으로 반환되므로 close(종료)가 필요 없읍
    print(sess.run(a)) #3
    print(a.eval()) #3
 ############################################

a = tf.constant(5)
b = tf.constant(3)
c = tf.multiply(a,b)  # c = a*b
d = tf.add(a,b)       # d = a+b
e = tf.add(c,d)       # e = c+d
sess = tf.Session()
print(sess.run(e))

############################################
inputdata = [1,2,3]
x = tf.placeholder(dtype=tf.int32) #실행시점의 데이터를 전달하는 노드
y = x*2
sess = tf.Session()
res = sess.run(y, feed_dict={x:inputdata})
print(res)


###############그래프 정의#############################
a = tf.placeholder(dtype=tf.float32)
b = tf.placeholder(dtype="float")
y = tf.multiply(a,b)
z = tf.add(y,y)

#그래프 실행#
sess = tf.Session()
print(sess.run(y, feed_dict={a:3, b:2}))

#a노드를 실행, 결과가 10이 출력
print(sess.run(a, feed_dict={a:10}))
#z노드를 실행, y는 a(3)*b(2) 값-> 12출력
print(sess.run(z, feed_dict={a:3, b:2}))

##################################################
x = tf.constant(15)
y = tf.Variable(x+5)

sess = tf.Session()
init = tf.global_variables_initializer() #변수 초기화
sess.run(init)
print(sess.run(y))

##################################################
inputdata = [1,2,3,4,5]
x = tf.placeholder(dtype=tf.float32)
w = tf.Variable(2, dtype=tf.float32)
y = tf.multiply(w,x)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(y, feed_dict={x:inputdata}))

################################################

x = tf.linspace(-1.0, 1.0, 10) #-1부터 1까지 10개의 구간으로 나눠라.
sess = tf.Session()
print(sess.run(x))
sess.close()

########################################################

a = tf.placeholder(dtype="float")
b = tf.placeholder(dtype="float")
y = tf.multiply(a,b)
z = tf.add(y,y)
with tf.Session() as sess:
    print(sess.run(z,feed_dict={a:4, b:4}))

###########################################################

x = tf.constant([[1.0, 2.0, 3.0]]) # 1행3열
w = tf.constant([[2.0], [2.0], [2.0]]) # 3행1열
y = tf.matmul(x,w) #(1,3)(3,1)바깥(1행,1열)의 형태로 값이 출력, 만약 (w,x)라면 (3,1)(1,3)이면 (3,3)의 형태로 출력
sess = tf.Session()
res = sess.run(y)
print(res)

###########################################################

x = tf.Variable([[1.0, 2.0, 3.0]]) # 1행3열
w = tf.constant([[2.0], [2.0], [2.0]]) # 3행1열
y = tf.matmul(x,w) # multiply로 하면 브로드캐스팅(eliment multiply)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
res = sess.run(y)
print(res)

print('='*50)
###########################################################
#              1회  2회  3회    1회  2회  3회    1회  2회  3회
input_data = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [2.0, 3.0, 4.0]] #3행3열
x = tf.placeholder(dtype=tf.float32, shape=[None,3]) # None:텐서플로우에서는 값이 정해져 있지 않은 상황을 의미, (행:?,열:3)
#모델을 만들기 위해 input_data(트레이닝 데이터)를 학습해감에 따라 열은 거의 고정 but 데이터가 쌓임에 따라 행은 증가하므로 행만 정의하지 않고 None으로 설정(ex.2016년도의 1회,2회,3회, 2017년도의 1회,2회,3회....)
w = tf.Variable([[2.0], [2.0], [2.0]]) #3행1열
y = tf.matmul(x,w) # multiply로 하면 브로드캐스팅(element multiply)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
res = sess.run(y, feed_dict={x:input_data})
print(res)

print('='*50)
###########################################################
input1 = tf.constant([3.0])
input2 = tf.constant([2.0])
input3 = tf.constant([5.0])
inter = tf.add(input2, input3)
mul = tf.multiply(input1, inter)
with tf.Session() as sess:
    res1, res2 = sess.run([mul, inter])
    mulres = sess.run(mul)
    mulinter = sess.run(inter)
# print(res[1])
print(res1)
print(res2)
print(mulres)
print(mulinter)