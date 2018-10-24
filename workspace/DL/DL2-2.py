import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.set_random_seed(777)

num_points = 1000 #(난수 1000개)
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55) #평균0, 표준편차0.55인 난수를 생성  # 정규분포:np.random.normal(size=5) 정규분포로부터 개수가 5개인 샘플을 추출
    y1 = x1*0.1+0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1,y1]) # [x,y] 1000쌍의 난수가 vector_set에 저장
# print(vectors_set)
print('='*50)
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]
# print(x_data)
# print('='*50)
# print(y_data)

plt.plot(x_data, y_data, 'ro')
# plt.show()

###############################################3
w = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) #random_uniform:균등분포, -1에서 1사이의 난수가 1개 발생, 난수 1개를 발생시켜서 변수의 값으로 초기화하는 작업을 w라는 이름의 노드로 정의, 난수 1개를 발생시켜서 w에게 주어라(w는 변수)
b = tf.Variable(tf.zeros(1))
hf = w * x_data + b #가설함수(예측함수)

cost = tf.reduce_mean(tf.square(hf - y_data)) # hf:예측값, y_data(실제값), square(제곱), reduce_mean:합의 평균

###################그래프 정의############################3
#  W:= W - a * cost함수에 대한 미분계수(+,-) # a(알파):0.1~0.01로 초기화 하는 게 일반적임(최적의 알파(a)값을 찾는 문제는 여전히 연구 분야)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)  # a * cost함수에 대한 미분계수(+,-)
train = optimizer.minimize(cost)  # cost가 낮아지도록 트레이닝
#변수 초기화
init = tf.global_variables_initializer()
###그래프 실행###
sess = tf.Session()
sess.run(init)

for step in range(101): #트레이닝을 101번 수행, 매 트레이닝 시 1000개 데이터에 대한 cost연산
    sess.run(train) # 1000개 데이터에 대해 1번씩 트레이닝 수행후, w(and b)갱신
    if step%10==0:  # 트레이닝 10회때마다 출력
        print(sess.run(w), sess.run(b))  # [0.7676065] [0.]
        print(sess.run(cost))  #1000개의 데이터에 대한 cost, 즉 hf = 0.7676065 * x + 0 (여기서 x는 1000개), 따라서 cost = hf - y(1000개)의 제곱의 합의 평균, 이 1000개의 데이터에 대한 학습을 거듭할 수록 cost는 작아짐
        plt.plot(x_data, y_data, 'ro')
        plt.plot(x_data, sess.run(w)*x_data+sess.run(b)) # sess.run(w)*x_data+sess.run(b) = h(x)예측값
        plt.xlabel('x')
        plt.xlim(-2, 2)
        plt.ylim(0.1, 0.6)
        plt.ylabel('y')
        # plt.show()


