from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

#  引入中文字体库
font = FontProperties(fname=r"./simsun.ttc", size=14)

#  使用np.linspace定义x：范围是(0,10);个数是100. 仿真一维数据组(x ,y)表示曲线1.
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建窗口
plt.figure(num=3, figsize=(8, 5), )

# 设置标题
plt.title("welcome matplotlib")

# 限制x轴、y轴
# plt.xlim((0, 10))
# plt.ylim((-1, 1))
plt.axis([-1, 11, -2, 2])

# 设置x轴y轴 label
plt.xlabel('x轴', FontProperties=font)
plt.ylabel('y轴', FontProperties=font)

# 描点画图
plt.plot(x, y1, color='red', linewidth=5.0, linestyle='--', label="six(x)函数")
plt.plot(x, y2, color='blue', linewidth=1.0, linestyle='-', label="cos(x)函数")
# 散点图绘制
plt.scatter(x, x ** 2, label="tan(x)")

# 使用np.linspace定义范围以及个数：范围是(0,10);个数是10. 使用plt.xticks设置x轴刻度：范围是(0,10);个数是10.
new_ticks = np.linspace(0, 10, 10)
plt.xticks(new_ticks)
# 使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’].
# plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 坐标边线
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 加载图示 label="six(x)"/label="cos(x)"
plt.legend(prop=font)

# 显示图像
plt.show()
