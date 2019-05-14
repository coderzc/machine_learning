import time

time_start=time.time()

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')

sess = tf.Session()

print(sess.run(hello))
time_end=time.time()





print('totally cost',time_end-time_start)