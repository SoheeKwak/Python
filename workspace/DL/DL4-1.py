import math
import matplotlib.pyplot as plt
print(math.e)

def sigmoid(z):
    return 1./ (1.+ math.e**-z)

print(sigmoid(-10)) #0에 가까운 값
print(sigmoid(0)) #0.5
print(sigmoid(5)) #무한대에 가까운 값

for i in range(-100, 100):
    z=i/10  # 정확힌 z=wx+b이지만 여기선 시각화를 위해 단순히 z를 설정
    s = sigmoid(z)
    plt.plot(z, s, 'ro')
# plt.show()

###############################################################################
def A():
    return  'A'
def B():
    return 'B'
y=1
print(y*A()+(1-y)*B()) #cost function과 비슷

###############################################################################
import tensorflow as tf
import numpy as np

def without_normalization():
    data = [[828.659973, 833.450012, 908100, 828.349976, 831.659973],
            [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
            [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
            [816, 820.958984, 1008100, 815.48999, 819.23999],
            [819.359985, 823, 1188100, 818.469971, 818.97998],
            [819, 823, 1198100, 816, 820.450012],
            [811.700012, 815.25, 1098100, 809.780029, 813.669983],
            [809.51001, 816.659973, 1398100, 804.539978, 809.559998]]

    print(np.shape(data))
    data = np.transpose(data)
    print(np.shape(data))
    x = data[:-1].transpose().astype(np.float32)
    y = data[-1:].transpose().astype(np.float32)
    print(x.shape)
    print(y.shape)
    #########그래프 정의##########
    w = tf.Variable(tf.random_uniform([4,1],-1,1)) # hf[8,1]= x[8,4]* w[4,1]
    b = tf.Variable(tf.random_uniform([1],-1,1))

    hf = tf.matmul(x,w) + b
    cost = tf.reduce_mean((hf-y)**2)
    lr = 0.000000001
    optimizer = tf.train.GradientDescentOptimizer(lr)
    train = optimizer.minimize(cost)

    ########세션 생성, 변수 초기화#####
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(201):
        sess.run(train)
        if i%5==0:
            print(i, sess.run(cost))  # data 3번째 열이 너무 갑자기 커져서 튀므로 train에서 발산하는 현상이 발생, 그래서 정규화를 시켜줘야 함.

############정규화##########
def min_max_scaler(data) :
    print(np.min(data)) #data 전체에 대한 최소값
    print(np.max(data)) #data 전체에 대한 최대값
    print("="*50)
    print(np.min(data, axis=0))  # data 각 열에 대한 최소값
    print(np.max(data, axis=0))  # data 각 열에 대한 최대값

    min = np.min(data, axis=0)
    max = np.max(data, axis=0)

    return (data-min)/(max-min)

data = [[828.659973, 833.450012, 908100, 828.349976, 831.659973],
        [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
        [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
        [816, 820.958984, 1008100, 815.48999, 819.23999],
        [819.359985, 823, 1188100, 818.469971, 818.97998],
        [819, 823, 1198100, 816, 820.450012],
        [811.700012, 815.25, 1098100, 809.780029, 813.669983],
        [809.51001, 816.659973, 1398100, 804.539978, 809.559998]]
print(min_max_scaler(data)) #data를 정규화한 결과 리턴

print("="*50)
def min_max_scaler_by_row(data) :
    min = np.min(data, axis=1)
    max = np.max(data, axis=1)
    print(min)
    print(min.shape) #(8,)
    print("=" * 50)
    print(max)  #(8,)
    print(max.shape)
    print(np.shape(data)) #(8, 5) #이 상태로는 shape이 안 맞아서 아래와 같이 transpose 해줌
    data = np.transpose(data)
    print(data.shape) #(5, 8)
    return (data-min)/(max-min)

data = [[828.659973, 833.450012, 908100, 828.349976, 831.659973],
        [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
        [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
        [816, 820.958984, 1008100, 815.48999, 819.23999],
        [819.359985, 823, 1188100, 818.469971, 818.97998],
        [819, 823, 1198100, 816, 820.450012],
        [811.700012, 815.25, 1098100, 809.780029, 813.669983],
        [809.51001, 816.659973, 1398100, 804.539978, 809.559998]]
print(min_max_scaler_by_row(data))

print("=" * 50)
##########표준화##########
def standard_scaler(data) :
    mean = np.mean(data)
    std = np.std(data)
    return (data-mean)/std

data = [[828.659973, 833.450012, 908100, 828.349976, 831.659973],
        [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
        [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
        [816, 820.958984, 1008100, 815.48999, 819.23999],
        [819.359985, 823, 1188100, 818.469971, 818.97998],
        [819, 823, 1198100, 816, 820.450012],
        [811.700012, 815.25, 1098100, 809.780029, 813.669983],
        [809.51001, 816.659973, 1398100, 804.539978, 809.559998]]
print(standard_scaler(data))




