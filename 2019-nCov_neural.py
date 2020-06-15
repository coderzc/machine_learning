import tensorflow as tf
import datetime
import matplotlib.pyplot as plt
import numpy as np
import requests
from matplotlib.font_manager import FontProperties
# Sequential 顺序模型
from keras import Sequential
# 神经网络,及激活函数
from keras.layers import Dense, Activation
# 随机梯度下降法
from keras.optimizers import SGD, Adam

from sklearn.preprocessing import StandardScaler, MinMaxScaler

font = FontProperties(fname=r"/Users/zc/PycharmProjects/machine_learning/simsun.ttc", size=14)
sdate = None


def load_data():
    # 拉取腾讯新闻数据
    res = requests.get('https://service-n9zsbooc-1252957949.gz.apigw.tencentcs.com/release/qq')
    res_json = res.json()
    data = res_json['data']['wuwei_ww_cn_day_counts']

    # 补充更早些的数据：
    data.append({'date': '01.11', 'confirm': '41', 'suspect': '0'})
    data.append({'date': '01.12', 'confirm': '41', 'suspect': '0'})
    data.sort(key=lambda x: x["date"])

    # 去掉最后一天(因为今天的数据不准要等，明天早上才会有准确的数据)
    # 因为20号以前并非是全国数据，数据不好要去掉
    data = data[10:]
    print(data)
    # 获取首次出现感染人数的日期
    global sdate
    sdate = datetime.datetime.strptime('2020.' + data[0]['date'], '%Y.%m/%d').date()

    x_data_history = [datetime.datetime.strptime('2020.' + dd['date'], '%Y.%m/%d').date().strftime("%m-%d") for dd in
                      data]
    t = [datetime.datetime.strptime('2020.' + dd['date'], '%Y.%m/%d').date() for dd in data]
    P_confirm = [int(dd['confirm']) for dd in data]
    P_suspect = [int(dd['suspect']) for dd in data]
    return np.array(t, dtype=np.datetime64), np.array(P_confirm), np.array(P_suspect), x_data_history


# 计算相隔天数
def day_delay(t):
    t0_date = np.datetime64(sdate, 'D')
    t_ = (t - t0_date)
    days = (t_ / np.timedelta64(1, 'D')).astype(int)
    return days


if __name__ == '__main__':
    #  日期及感染人数
    t, P_confirm, P_suspect, x_show_data = load_data()
    x_data, y_data = day_delay(t), P_confirm

    '''
    数据归一化
    一、数据标准化
    StandardScaler (基于特征矩阵的列，将属性值转换至服从正态分布)
    标准化是依照特征矩阵的列处理数据，其通过求z-score的方法，将样本的特征值转换到同一量纲下
    常用与基于正态分布的算法，比如回归
    二、数据归一化
    MinMaxScaler （区间缩放，基于最大最小值，将数据转换到0,1区间上的）
    提升模型收敛速度，提升模型精度
    常见用于神经网络
    三、Normalizer （基于矩阵的行，将样本向量转换为单位向量）
    其目的在于样本向量在点乘运算或其他核函数计算相似性时，拥有统一的标准
    常见用于文本分类和聚类、logistic回归中也会使用，有效防止过拟合
    '''
    min_max_scaler = MinMaxScaler().fit(x_data[:, np.newaxis])
    x_data_scaler = min_max_scaler.transform(x_data[:, np.newaxis])

    min_max_scaler_y = MinMaxScaler().fit(y_data[:, np.newaxis])
    y_data_scaler = min_max_scaler_y.transform(y_data[:, np.newaxis])

    # 构建一个顺序模型
    model = Sequential()
    # 在模型中添加一个全连接层
    model.add(Dense(50, activation='sigmoid', input_dim=1))
    model.add(Dense(1))
    model.add(Dense(30, activation='sigmoid'))
    model.add(Dense(1))

    # 编译模型
    adam = Adam(lr=0.001)
    model.compile(loss='mse', optimizer=adam)

    # 训练
    model.fit(x_data_scaler, y_data_scaler, epochs=10000)

    # 预测
    future = np.linspace(0, 35, 35)
    x_show_data_all = [(sdate + (datetime.timedelta(days=fu))).strftime("%m-%d") for fu in future]
    future = future[:, np.newaxis]
    future_scaler = min_max_scaler.transform(future)
    future_predict = model.predict(future_scaler)

    # 绘图
    plt.scatter(x_show_data, y_data, s=35, c='green', marker='.', label="确诊人数")
    plt.plot(x_show_data_all, min_max_scaler_y.inverse_transform(future_predict), 'r-s', marker='+', linewidth=1.5,
             label='预测曲线')

    plt.tick_params(labelsize=5)
    plt.xlabel('时间', FontProperties=font)
    plt.ylabel('感染人数', FontProperties=font)
    plt.xticks(x_show_data_all)
    plt.grid()  # 显示网格
    plt.legend(prop=font)  # 指定legend的位置右下角
    plt.show()
