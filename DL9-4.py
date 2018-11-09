import tensorflow as tf
import numpy as np

data = np.loadtxt('data.csv',delimiter=',',unpack='True', dtype='float32',encoding='utf-8') #unpack='True' 전체데이터 transpose
# print(data)
xdata = np.transpose(data[0:2])
ydata = np.transpose(data[2:])
print("=========")
# print(xdata)
# print(ydata)

## 신경망 모델 생성 ##
global_step = tf.Variable(0, trainable=False, name='global_step')
#global_step:모델 저장과정에서 사용될 변수, 초기값:0
#trainable=False:트레이닝용 데이터에서 제외됨, 학습 횟수를 count하는 변수
X = tf.placeholder(tf.float32) #None,2
y = tf.placeholder(tf.float32)#None,3

W1 = tf.Variable(tf.random_uniform([2,10],-1.,1.)) #신경망이므로 (2,3)이 아닌 hidden layer의 노드이므로 임의로 10개의 feature를 가졌다고 설정
L1 = tf.nn.relu(tf.matmul(X,W1)) #relu는 무조건 0이상의 값이 출력.

W2 = tf.Variable(tf.random_uniform([10,20],-1.,1.)) #다음 hidden layer의 노드로 임의의 20개 feature를 가졌다고 설정
L2 = tf.nn.relu(tf.matmul(L1,W2))

W3 = tf.Variable(tf.random_uniform([20,3],-1.,1.))
model = tf.matmul(L2,W3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y, logits=model))
optimizer = tf.train.AdamOptimizer(0.01)
train = optimizer.minimize(cost, global_step=global_step) #트레이닝을 1회 끝날때마다 최적회된 모델, global_step 1, 2, 3..의 모델이 생성됨

#######신경망 모델 생성(학습)##########
sess = tf.Session()
saver = tf.train.Saver(tf.global_variables()) #모델 저장:Variables(변수)를 가져와 저장하는 함수. 즉, w, b를 파일로 저장
ckpt = tf.train.get_checkpoint_state('./model') #get_checkpoint_state: model 폴더 안에 기존에 학습된 모델이 저장돼 있는지 확인하는 변수
if ckpt and tf.train.checkpoint_exists(ckpt.model_checkpoint_path): #모델이 저장된 폴더가 존재, and 모델이 만들어져 있다면
    saver.restore(sess, ckpt.model_checkpoint_path) #./model폴더에 기존에 저장된 모델이 있으면 global_variables를 복원
else:
    sess.run(tf.global_variables_initializer())  #처음 학습 시 모델이 없으므로 변수 초기화, 이후부터는 위(saver.restore)에서 기존의 모델을 복원해 추가 학습 수행

for step in range(2):
    sess.run(train, feed_dict={X:xdata, y:ydata}) 
    print('step: %d' % sess.run(global_step),
          'cost: %.3f'%sess.run(cost, feed_dict={X:xdata, y:ydata}))
saver.save(sess, './model/dnn.ckpt', global_step) #2회 트레이닝 끝난 후 './model/dnn.ckpt'파일명의 global_step횟수와 함께 세션이 새로 생성된 model폴더에 저장