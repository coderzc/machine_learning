from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

#  引入中文字体库
# font = FontProperties(fname=r"./Songti.ttc", size=14)

#  使用np.linspace定义x：范围是(-1,1);个数是50. 仿真一维数据组(x ,y)表示曲线1.
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x**2

# 创建窗口
plt.figure(num=3, figsize=(8, 5), )

# 限制x轴、y轴
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置x轴y轴 label
plt.xlabel('x')
plt.ylabel('y')

# 描点画图
plt.plot(x, y1, color='red', linewidth=5.0, linestyle='--')
plt.plot(x, y2, color='blue', linewidth=1.0, linestyle='-')

# 使用np.linspace定义范围以及个数：范围是(-1,2);个数是5. 使用plt.xticks设置x轴刻度：范围是(-1,2);个数是5.
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# 使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’].
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 坐标边线
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 显示图像
plt.show()
