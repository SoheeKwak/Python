## corpus(말뭉치):특정 도메인에 등장하는 단어들의 집합

#1. 10개의 문장 수집 -> 워드 벡터 생성
corpus = ['boy is a young man',
          'girl is a young woman',
          'queen is a wise woman',
          'king is a strong man',
          'princess is a young queen',
          'prince is a young king',
          'woman is pretty',
          'man is strong',
          'princess is a girl will be queen',
          'prince is a boy will be king']

#2. 불필요한 단어 제거
def remove_stop_words(corpus):
    # it's-> it is 등의 전처리 작업
    stop_words = ['is','a','will','be']
    results=[]
    for text in corpus:
        #print(text)
        tmp = text.split(' ')
        # print(tmp)
        for stop_word in stop_words:
            if stop_word in tmp:
                tmp.remove(stop_word)
        print(tmp)
        results.append(" ".join(tmp))
    return results

corpus = remove_stop_words(corpus) #corous에 위에서 리턴된 results가 들어감

words = []
for text in corpus:
    for word in text.split(' '):
        words.append(word)
words = set(words) #set: 중복 단어 제거
print(words)

word2int={}
for i, word in enumerate(words):
    print(i, word)
    word2int[word]=i
print(word2int) #{'wise': 11, 'queen': 1,....}

sentences=[]
for sentence in corpus:
    sentences.append(sentence.split())
print("sentences:",sentences)

#skipgram 적용, window size:2
WINDOW_SIZE = 2
"""
['boy', 'young', 'man'] 좌로 2칸, 우로 2칸까지 모두 참조
xdata ydata
boy   young
boy   man
young boy
young man
man   boy
man   young
"""
data=[]
for sentence in sentences:
    print(sentence)
    for idx, word in enumerate(sentence): #word: boy
        print(idx, word)
        for neighbor in sentence[ #['boy', 'young', 'man']...
                        max(idx-WINDOW_SIZE,0): #max(0-2, 0)=>0, min(0+2, 3)+1=>3 즉, 최소0에서 최대3까지만 허용
                        min(idx+WINDOW_SIZE, len(sentence))+1]: #[0:3]의 범위로 정해주는 설정(WINDOW SIZE:2)
            if neighbor!=word:
                data.append([word, neighbor])
print("data:",data)

import pandas as pd
for text in corpus:
    print("corpus:", text)
df = pd.DataFrame(data, columns=['input', 'label'])
print(df)
print(df.shape)#(52, 2)


########### deep learning##############
import tensorflow as tf
import numpy as np

ONE_HOT_DIM = len(words)#중복되지 않은 단어들의 개수

def to_one_hot_encoding(data_point_index):
    to_one_hot_encoding = np.zeros(ONE_HOT_DIM)
    to_one_hot_encoding[data_point_index]=1
    return to_one_hot_encoding
X=[] #input
Y=[] #target

for x,y in zip(df['input'],df['label']):
    X.append(to_one_hot_encoding(word2int[x]))
    Y.append(to_one_hot_encoding(word2int[y]))
print(X) #input
print(Y) #label


xtrain = np.asarray(X)
ytrain = np.asarray(Y)
#텐서플로우에서 사용하기 위한 다차원 배열로 변경
x = tf.placeholder(tf.float32, shape=(None, ONE_HOT_DIM))
ylabel = tf.placeholder(tf.float32, shape=(None, ONE_HOT_DIM))

EMBBDDING_DIM=2 #weight를 2개 줌

#히든 계층(워드 벡터)                     #(11, 2)
W1 = tf.Variable(tf.random_normal([ONE_HOT_DIM, EMBBDDING_DIM]))
b1 = tf.Variable(tf.random_normal([EMBBDDING_DIM])) #EMBBDDING_DIM 대신 1써도 됨, but 어차피 최종 출력은 1이므로
hidden_layer = tf.add(tf.matmul(x,W1),b1)

W2 = tf.Variable(tf.random_normal([EMBBDDING_DIM, ONE_HOT_DIM]))
b2 = tf.Variable(tf.random_normal([1]))
prediction = tf.nn.softmax(tf.add(tf.matmul(hidden_layer, W2), b2))

cost = tf.reduce_mean(-tf.reduce_sum(ylabel*tf.log(prediction), axis=1))
train = tf.train.GradientDescentOptimizer(0.05).minimize(cost)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

iteration = 20000
for i in range(iteration):
    sess.run(train, feed_dict={x:xtrain, ylabel:ytrain})
    if i %3000==0:
        print('interation'+str(i)+'cost is:',
              sess.run(cost, {x:xtrain, ylabel:ytrain}))

print(sess.run(W1+b1))

vextors = sess.run(W1+b1)
df2 = pd.DataFrame(vextors, columns=['x1','x2'])
df2['word']=words
df2 = df2[['word','x1','x2']]
print(df2)

import matplotlib.pyplot as plt
fig,ax = plt.subplots()
for word, x1, x2 in zip(df2['word'],df2['x1'],df2['x2']):
    ax.annotate(word, (x1,x2))  #word로 좌표 위 구현
padding=1.0
x_axis_min = np.amin(vextors,axis=0)[0]-padding
y_axis_min = np.amin(vextors,axis=0)[1]-padding
x_axis_max = np.amax(vextors,axis=0)[0]+padding
y_axis_max = np.amax(vextors,axis=0)[1]+padding
plt.xlim(x_axis_min, x_axis_max)
plt.ylim(y_axis_min, y_axis_max)
plt.rcParams["figure.figsize"]=(10,10)
plt.show()
