import tensorflow as tf

sess = tf.Session()
myqueue = tf.train.string_input_producer(['q_1.txt','q_2.txt','q_3.txt'], shuffle=False) #default가 shuffle

reader = tf.TextLineReader()
key, value = reader.read(myqueue) #실제 데이터는 value에 들어감
record_default=[[-1],[999]] #값이 없을 때 x(sp):-1, y(dist):999 입력
sp, dist = tf.decode_csv(value, record_defaults=record_default)

x_batch, y_batch = tf.train.batch([sp, dist], batch_size=4) #한번에 4개씩 읽기

coord = tf.train.Coordinator() #파일 3개를 읽기 위한 협력 명령, 각 파일에 대해 협력자인 각 threads(여기선 3개)필요
threads = tf.train.start_queue_runners(sess=sess,coord=coord)

for i in range(100):
    x,y = sess.run([x_batch, y_batch])
    #x,y로 모델링
    print(x,y)
coord.request_stop()
coord.join(threads=threads)

