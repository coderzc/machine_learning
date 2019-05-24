import tensorflow as tf

'''
几种常见的Tensor

Const(常量)

Variable(变量)

Placeholder(占位符)
'''

constant = tf.constant([1, 2, 3, 4, 5, 6, 7])

print(constant)

variable = tf.Variable(1)

print(variable)

variable2 = tf.Variable(1., dtype=tf.float32)

print(variable2)

tf.placeholder()