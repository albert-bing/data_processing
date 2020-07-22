# -*- encoding:utf-8 -*-
# 开发团队：大数据组
# 开发者：albert·bing
# 开发时间：2020/7/5 20:13
# 文件名称：yellow_calendar.py
# 开发工具：PyCharm


#  start your code

import xlrd

def select_event_id():
    sb = xlrd.open_workbook('E:\项目文件\开发文件\select_result\query-hive-6770.xlsx')
    sheet = sb.sheets()[0]
    list_all = []
    for ss in range(0, sheet.nrows):
        cells = sheet.row_values(ss)
        data = cells[1]
        list = data.replace('[', '').replace(']', '').replace('"', '').split(",")
        tup = [cells[0], list]
        print(tup)
        list_all.append(tup)
    return list_all

def read_s202m():
    s202 = xlrd.open_workbook('E:\项目文件\开发文件\S202M埋点.xlsx')

    laucher = s202.sheets()[0]
    # 车辆设置
    car_setting = s202.sheets()[1]
    # 系统设置
    system_setting = s202.sheets()[2]
    # 空调
    air_conditioning = s202.sheets()[3]




if __name__ == '__main__':
    select_event_id()