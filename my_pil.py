from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
'''
更多关于图片处理库：
https://blog.csdn.net/renelian1572/article/details/78761278
https://blog.csdn.net/dss875914213/article/details/84974472
'''


# 显示图片
def show_img(img):
    plt.figure("beauty")
    plt.imshow(img)
    plt.axis('off')
    plt.title('test image')
    plt.show()

# 打开图片
img = Image.open("/Users/zc/Downloads/cat.jpg")
origin_array = np.asarray(img)
print('origin_array:\n', origin_array)

# 压缩
img = img.resize((128, 128), Image.ANTIALIAS)

# 二值化
gray_1 = img.convert('1')
print(np.asarray(gray_1))

# 灰度化
gray_L = img.convert('L')
gray_l_array = np.asarray(gray_L)
print(gray_l_array)
print(gray_l_array.dtype)
