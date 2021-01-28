# -*- encoding:utf-8 -*-
# 开发团队：大数据组
# 开发者：albert·bing
# 开发时间：2020/7/5 20:13
# 文件名称：yellow_calendar.py
# 开发工具：PyCharm


#  start your code

import xlrd
import xlwt
import faker


def select_event_id():
    sb = xlrd.open_workbook('E:\项目文件\开发文件\select_result\query-hive-6829.xlsx')
    sheet = sb.sheets()[0]
    list_all = []
    for ss in range(0, sheet.nrows):
        cells = sheet.row_values(ss)
        data = cells[1]
        list = data.replace('[', '').replace(']', '').replace('"', '').split(",")
        tup = [cells[0], list]
        # print(tup)
        list_all.append(tup)
    return list_all


# s202的所有事件
def read_s202m():
    s202 = xlrd.open_workbook('E:\项目文件\开发文件\S202M埋点.xlsx')

    normal_list = []

    # 启动
    laucher = s202.sheets()[0]
    normal_list.append(for_utils(laucher, 2))
    # 车辆设置
    car_setting = s202.sheets()[1]
    normal_list.append(for_utils(car_setting, 2))
    # 系统设置
    system_setting = s202.sheets()[2]
    normal_list.append(for_utils(system_setting, 2))
    # 空调
    air_conditioning = s202.sheets()[3]
    normal_list.append(for_utils(air_conditioning, 1))
    # 用户中心
    user_center = s202.sheets()[4]
    normal_list.append(for_utils(user_center, 2))
    # 声音
    voice = s202.sheets()[5]
    normal_list.append(for_utils(voice, 2))
    # 系统
    system = s202.sheets()[6]
    normal_list.append(for_utils(system, 2))
    # 地图
    map = s202.sheets()[7]
    normal_list.append(for_utils(map, 1))
    # 幻月
    magic_moon = s202.sheets()[8]
    normal_list.append(for_utils(magic_moon, 2))
    # 音乐
    music = s202.sheets()[9]
    normal_list.append(for_utils(music, 2))
    # 电台
    radio_station = s202.sheets()[10]
    normal_list.append(for_utils(radio_station, 2))

    return normal_list


def read_s202h():
    pass


def read_s203ev():
    pass


def for_utils(event_data, number_cell):
    normal = []
    for ll in range(1, event_data.nrows):
        cells = event_data.row_values(ll)
        normal.append(cells[number_cell])
    # print(normal)
    return normal


if __name__ == '__main__':
    source_list = select_event_id()
    # print(source_list[8][1])
    source_list1 = source_list[8][1]
    normal_list_all = read_s202m()
    all = []
    num = 0
    for nn in range(0, len(normal_list_all), 1):
        for mm in range(0, len(normal_list_all[nn])):
           all.append(normal_list_all[nn][mm])

    print(all)
    print()
    # 制定有，未上报的
    res1 = list(set(all).difference(set(source_list1)))
    print("制定有，未上报的",res1)
    # 上报有，未制定
    res2 = list(set(source_list1).difference(set(all)))
    print("上报有，未制定:",res2)
    # 共同拥有的
    res3 = list(set(all).intersection(set(source_list1)))
    print("共同拥有的:",res3)

    workbook = xlwt.Workbook()
    f = faker.Faker("zh_CN")
    sheet = workbook.add_sheet("s202M",cell_overwrite_ok=True)
    sheet.write(0, 0, label="制定有，未上报")
    sheet.write(0, 1, label="上报有，未制定")
    sheet.write(0, 2, label="共同拥有")
    for i in range(1,(max(len(res1),len(res2),len(res3)))):
        try:
            sheet.write(i, 0, label=res1[i])
        except Exception:
            pass
        try:
            sheet.write(i, 1, label=res2[i])
        except Exception:
            pass
        try:
            sheet.write(i, 2, label=res3[i])
        except Exception:
            pass

    workbook.save("E:\\项目文件\\开发文件\\res.xls")