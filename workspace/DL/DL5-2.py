import tensorflow as tf

sess = tf.Session()
myqueue = tf.train.string_input_producer(['q_1.txt','q_2.txt','q_3.txt'], shuffle=False) #default가 shuffle

coord = tf.train.Coordinator() #파일 3개를 읽기 위한 협력 명령, 각 파일에 대한 각 협력자인(여기선 3개)threads필요
threads = tf.train.start_queue_runners(sess=sess,coord=coord)

reader = tf.TextLineReader()
key, value = reader.read(myqueue) #실제 데이터는 value에 들어감
print(sess.run(key))
print(sess.run(value))
rd=[[0],[0]] #결측치는 0으로 채워넣음
for i in range(100):
    sp, dist = tf.decode_csv(value, record_defaults=rd)
    print(sess.run([sp,dist]))
coord.request_stop()
coord.join(threads=threads)

