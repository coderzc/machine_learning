# numpy  基础知识
import numpy as np

'''
快速创建N维数组的api函数
'''
# 创建10行10列的数值为浮点0的矩阵
print("np.zeros\n", np.zeros([10, 10]))

# 创建10行10列的数值为浮点1的矩阵
print("np.ones\n", np.ones([10, 10]))

# 创建10行10列的数值为浮点1的对角矩阵
print("np.eye\n", np.eye(10, 10))

# 从数值范围创建数组 开始，结束，步长，输出元素类型
print("np.arange\n", np.arange(0, 100, 2, float))

# 生产随机数组 5行5列 范围0～1
print(np.random.rand(5, 5))

# 生成在半开半闭区间 [low,high)上离散均匀分布的整数值;若high=None，则取值区间变为[0,low) ; size维度
print(np.random.randint(4, 10, size=(5, 5)))

# 给定均值/标准差/维度的正态分布
print(np.random.normal(1.75, 0.1, (3, 4)))

# 将列表转换为np数组
array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

np_array = np.array(array, dtype=float)  # copy,新数组
print("np.array:\n", np_array)

np_array2 = np.asarray(array, dtype=float)  # view,会改变原数组
print("np.asarray:\n", np_array2)

'''
查看数组属性
'''
# 数组元素个数
print("数组元素个数 size:", np_array.size)
# 数组形状
print("数组形状 shape:", np_array.shape)
# 数组维度
print("数组维度 ndim:", np_array.ndim)
# 数组元素类型
print("数组元素类型 dtype:", np_array.dtype)
# 数组中每个元素的字节大小
print("数组元素类型 itemsize:", np_array.itemsize)

'''
shape操作
'''
array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
n1 = np.asarray(array)

# 改变数组的格式
n2 = n1.reshape(6, 2)
print(n1)
print(n2)

# 将多维降到1维展开
print("flatten():", n2.flatten())  # copy,新数组
print("ravel():", n2.ravel())  # view，会改变原数组,却不会改变shape

# 转置
n3 = np.arange(12)
n3 = n3.reshape(3, 4)
print("n3:", n3)
print("T:", n3.T)

# reshape一些特殊值
n4 = np.arange(10, 130, 10)
print("n4:", n4.reshape(4, 3))
#   -1 一维展开 与 ravel()作用相似
print(n4.reshape(-1))
#   (-1,1) n行，1列
print(n4.reshape(-1, 1))
#   (1,-1) 1行，n列但任然是二维矩阵
print(n4.reshape(1, -1))

'''
数组索引和迭代
'''
print('\n\n')
n5 = np.arange(30)
print('n5:', n5)
# 获取第一个元素
print(n5[0])
# 获取倒数第一个元素
print(n5[-1])
# 取前十个数
print(n5[:10])
# 取后十个数
print(n5[-10:])
# 取前11-20个数，左闭右开
print(n5[10:20])
# 前十个数中，每2个数取一个
print(n5[:10:2])
# 第6-15个数中，每3个数取一个
print(n5[5:15:3])
# 所有的数中，每10个数取一个
print(n5[::10])
# 什么都不写，可以原样复制一个数组
print(n5[:])

# 多维数组索引与切片
n6 = n5.reshape(5, 6)
print('\nn6:', n6)
# 索引第二行第三列
print('n6[1, 2]:\n', n6[1, 2])
# 在第一维取前两行，第二维每+2取一个元素
print('n6[:2, ::2]:\n', n6[:2, ::2])
# 取第一列
print('n6[:, 0]]:\n', n6[:, 0])
# 取第2、3列
print('n6[:, 3:5]]:\n', n6[:, 3:5])

'''
基础运算
'''
n7 = np.asarray([10, 20, 30, 40])
n8 = np.arange(4)
print(n7)
print(n8)

# 计算立方
print(n7 ** 3)

# 三角函数
print(np.sin(n7))

# 指定轴最大/小值
print(np.amax(n7, axis=0))
print(np.amin(n7, axis=0))

# 平均值
print(np.mean(n7, axis=0))

# 标准差
print(np.std(n7, axis=0))

# 两个np相减
print("n7-n8:", n7 - n8)

n9 = np.asarray([[1, 1], [0, 1]])
n10 = np.arange(4).reshape((2, 2))

# 两个np逐位相乘（非矩阵乘法）
print(n9 * n10)

'''
矩阵运算
'''
A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
B = np.transpose(np.array([[-3, 5, -2]]))
x = np.linalg.solve(A, B)
print('x:\n', x)

# 矩阵乘法
A = np.array([[3, 2, -2], [3, 1, 4], [3, 1, -2]])
B = np.arange(9).reshape((3, 3))
C = np.dot(A, B)
print('C:\n', C)
