# -*- encoding:utf-8 -*-
# 开发团队：大数据组
# 开发者：albert·bing
# 开发时间：2020/7/5 20:13
# 文件名称：yellow_calendar.py
# 开发工具：PyCharm


#  start your code

# import sys
# sys.path.append('/home/hadoop/programs/spider/WTP66_BigdataCrawler')
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import os
import time

def drawing(list_add_num,list_add_hour,title):
    # list_add_num,list_add_hour,title
    # list_add_hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    # list_add_num = [14, 9, 7, 5, 2, 2, 14, 31, 37, 44, 47, 40, 44, 39, 38, 45, 52, 44, 39, 28, 37, 31, 20,12]
    # title='万宁市'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    # 设置画布大小
    fig = plt.figure(figsize=(20,15))

    font1 = {'family': 'sans-serif',
             'weight': 'normal',
             'size': 16,
             }

    # fig.suptitle('产地在各个国家所在的数量', fontsize = 24, fontweight = 'bold')
    # 绘制图形
    plt.bar(range(len(list_add_num)), list_add_num, align='center', color='red', alpha=0.8)
    # 标题
    plt.title(title)
    # x轴设置
    plt.xticks(np.arange(len(list_add_hour)), list_add_hour)
    # plt.xticks(x,list_add_name)
    # y轴设置
    # plt.ylim([0,500])
    # plt.xlim([0,60])
    # 设置条形图所代表的数量
    for x, y in enumerate(list_add_num):
        plt.text(x, y + 2, '%s' % round(y, 1), ha='center')
    # 折线图
    plt.plot(range(len(list_add_hour)), list_add_num, marker='o', color='coral')
    # x，y轴的说明
    plt.xlabel('时间', font1)
    plt.ylabel('数量', font1)
    # 绝对位置保存
    plt.savefig(os.path.join(os.path.abspath('D:\project\code_python\data_processing\com\wt\channel_event\citys\郑州'), title + '.png'))
    # 关闭保存时打开的图片，防止内存溢出
    plt.close()
    # 相对位置保存
    # plt.savefig(title+'.png')
    # 显示图片
    # plt.show()

def get_data(data):
    m = 0
    list_add_num = []
    list_add_hour = []
    title = ""
    for i in range(0,len(data), 1):
        m = m + 1
        if data[i:i + 1]['hour'].values[0] == 23:
            list_add_num.append(data[i:i + 1]['nums'].values[0])
            list_add_hour.append(data[i:i + 1]['hour'].values[0])
            print(title)
            print(list_add_hour)
            print(list_add_num)
            drawing(list_add_num,list_add_hour,title)
            time.sleep(1)
            list_add_num = []
            list_add_hour = []
            m = 1
        else:
            list_add_num.append(data[i:i+1]['nums'].values[0])
            list_add_hour.append(data[i:i+1]['hour'].values[0])
            title = str(data[i:i+1]['ymd'].values[0]) + "-" + str(data[i:i+1]['city_name'].values[0])




if __name__ == '__main__':
    iris_data = pd.read_csv('zhengzhou.csv', error_bad_lines=False, encoding='gbk')
    iris_data.columns = ['ymd','city_name', 'hour', 'nums']

    get_data(iris_data)

    # drawing()

