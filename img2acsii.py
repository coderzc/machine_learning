from PIL import Image, ImageDraw, ImageFont
import argparse
import matplotlib.pyplot as plt

'''
把图片转化为acsii字符
'''


# 将256灰度映射到字符集上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    # 字符库
    ascii_char = list("   ...',;:clodxkO0KXNWMMMM")
    # ascii_char=list("##XXxxx+++===---;;,,...  ")
    # ascii_char=list(' .:-=+*#%@')
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)
    length = len(ascii_char)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


# 使用plt 显示图片
def show_img(img):
    plt.figure("Test")
    plt.title('Test image')
    plt.axis('off')  # 不显示坐标轴
    plt.imshow(img)
    plt.show()


# 输出到图像
def print_img(txt):
    # 计算ascii图事迹大小
    img_new = Image.new('RGB', (0, 0), (0, 0, 0))
    width, height = ImageDraw.Draw(img_new).textsize(txt)

    img_new = Image.new('RGB', (width, height), (0, 0, 0))
    d = ImageDraw.Draw(img_new)
    d.text((0, 0), txt, fill=(255, 255, 255))
    show_img(img_new)


if __name__ == '__main__':
    # 命令行输入参数处理
    parser = argparse.ArgumentParser()
    parser.add_argument('file')  # 输入文件
    parser.add_argument('-o', '--output')  # 输出文件
    parser.add_argument('-w', '--wight', type=int, default=80)  # 输出字符画宽
    parser.add_argument('-height', '--height', type=int, default=0)  # 输出字符画高

    # 获取参数
    args = parser.parse_args()
    IMG = args.file
    WIDTH = args.wight
    HEIGHT = args.height
    OUTPUT = args.output

    # 打开图片
    img = Image.open(IMG)

    # 压缩,调整图像比例
    w, h = img.size
    h_ = 0
    if HEIGHT == 0:
        h_ = int(((WIDTH * h) / w) * 0.40)
    else:
        h_ = HEIGHT
    img = img.resize((WIDTH, h_), Image.NEAREST)

    # 转化为真彩色(加透明度)
    rgba_img = img.convert('RGBA')

    txt = ""

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            # txt += '\033[34m' + get_char(*rgba_img.getpixel((j, i))) + '\033[0m' # 蓝色字符
            txt += get_char(*rgba_img.getpixel((j, i)))
        txt += '\n'

    # print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)

    # 输出到图像
    print_img(txt)
