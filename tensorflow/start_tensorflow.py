import tensorflow as tf

# 创建一个常量操作
hello = tf.constant('Hello, TensorFlow!')

# 启动一个 tensorflow Session(会话)
sess = tf.Session()

# 运行一个 tensorflow Graph(计算图)
print(sess.run(hello))

# 关闭Session
sess.close()
