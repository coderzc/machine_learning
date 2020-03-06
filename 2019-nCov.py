#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
拟合2019-nCov肺炎感染确诊人数
https://blog.csdn.net/weixin_36474809/article/details/104101055
"""
import datetime

import matplotlib.pyplot as plt
import numpy as np
import requests
from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

#  引入中文字体库

font = FontProperties(fname=r"./simsun.ttc", size=14)
sdate = None
hyperparameters_r = None
hyperparameters_K = None


def load_data():
    # 拉取腾讯新闻数据
    res = requests.get('http://service-n9zsbooc-1252957949.gz.apigw.tencentcs.com/release/qq')
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


def logistic_increase_function(t, K, P0):
    r = hyperparameters_r
    # K = hyperparameters_K
    # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
    exp_value = np.exp(r * (t))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)


if __name__ == '__main__':
    #  日期及感染人数
    t, P_confirm, P_suspect, x_show_data = load_data()
    x_data, y_data = day_delay(t), P_confirm

    # 分隔训练测试集,将最后的30%数据作为测试集
    x_train, x_test, y_train, y_test = x_data[:-1 * int(len(x_data) * 0.3)], x_data[
                                                                             -1 * int(len(x_data) * 0.3):], y_data[
                                                                                                            :-1 * int(
                                                                                                                len(
                                                                                                                    x_data) * 0.3)], y_data[
                                                                                                                                     -1 * int(
                                                                                                                                         len(
                                                                                                                                             x_data) * 0.3):]
    print(x_train)
    print(x_test)
    popt = None
    mse = float("inf")
    r = None
    k = None
    # 网格搜索优化r和K参数
    # for k_ in np.arange(44990, 50000, 1):
    #     hyperparameters_K = k_
    for r_ in np.arange(0, 1, 0.01):
        # 用最小二乘法估计拟合
        hyperparameters_r = r_
        popt_, pcov_ = curve_fit(logistic_increase_function, x_train, y_train)
        # # 获取popt里面是拟合系数
        print("K:capacity  P0:initial_value   r:increase_rate")
        # print(k_, popt_, r_)

        # 计算均方误差对测试集进行验证
        mse_ = mean_squared_error(y_test, logistic_increase_function(x_test, *popt_))
        print("mse:", mse_)
        if mse_ <= mse:
            mse = mse_
            popt = popt_
            r = r_
            # k = k_
    hyperparameters_K = k
    hyperparameters_r = r
    print("----------------")
    print("hyperparameters_K:", hyperparameters_K)
    print("hyperparameters_r:", hyperparameters_r)
    print("----------------")
    popt, pcov = curve_fit(logistic_increase_function, x_data, y_data)
    print("K:capacity  P0:initial_value   r:increase_rate")
    print(hyperparameters_K, popt, hyperparameters_r)
    # y_data_suspect = P_suspect
    # popt_suspect, pcov_suspect = curve_fit(logistic_increase_function, x_data, y_data_suspect)
    # # # 获取popt里面是拟合系数
    # print("K:capacity  P0:initial_value   r:increase_rate")
    # print(popt_suspect)

    # 未来预测
    future = np.linspace(0, 35, 35)
    future = np.array(future)
    future_predict = logistic_increase_function(future, *popt)
    # future_predict_suspect = logistic_increase_function(future, *popt_suspect)

    # 绘图
    x_show_data_all = [(sdate + (datetime.timedelta(days=fu))).strftime("%m-%d") for fu in future]
    plt.scatter(x_show_data, P_confirm, s=35, c='green', marker='.', label="确诊人数")
    # plt.scatter(x_show_data, P_suspect, s=30, c='orange', marker='.', label="疑似人数")
    plt.plot(x_show_data_all, future_predict, 'r-s', marker='+', linewidth=1.5, label='预测曲线')
    # plt.plot(x_show_data_all, future_predict_suspect, 'b-s', color='steelblue', marker='*', linewidth=1.0,
    #          label='预测疑似曲线')

    plt.tick_params(labelsize=5)
    plt.xlabel('时间', FontProperties=font)
    plt.ylabel('感染人数', FontProperties=font)
    plt.xticks(x_show_data_all)
    plt.grid()  # 显示网格

    plt.legend(prop=font)  # 指定legend的位置右下角
    plt.show()
