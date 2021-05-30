# -*- coding: utf-8 -*-


# 对数据的分布分析

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False

datafile = '../data/cleaned_data.csv'  # 原始数据,第一行为属性标签

# 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data = pd.read_csv(datafile, encoding='utf-8')

print(data.iloc[1, :])

# 用户性别探索
male = pd.value_counts(data['性别gender'])[1]
female = pd.value_counts(data['性别gender'])[0]
# 绘制会员性别比例饼图
fig = plt.figure(figsize=(7, 4))  # 设置画布大小
plt.pie([male, female], labels=['男', '女'], colors=['lightskyblue', 'lightcoral'], autopct='%1.1f%%')
plt.title('用户性别比例')
plt.show()


# 用户年龄探索
age = data['年龄age']
year = data['现职位工作年数employ']
time = data['服务月数tenure']

# 绘制年龄分布箱型图
plt.boxplot((age, year, time), patch_artist=True,
            labels=['年龄', '现岗位工作时间', '服务月数'],  # 设置x轴标题
            boxprops={'facecolor': 'lightblue'})  # 设置填充颜色
plt.title('用户年龄箱线图')
# 显示y坐标轴的底线
plt.grid(axis='y')
plt.show()


# 不同受教育水平人数探索
lv_0 = pd.value_counts(data['受教育水平ed'])[0]
lv_1 = pd.value_counts(data['受教育水平ed'])[1]
lv_2 = pd.value_counts(data['受教育水平ed'])[2]
lv_3 = pd.value_counts(data['受教育水平ed'])[3]
lv_4 = pd.value_counts(data['受教育水平ed'])[4]
# 绘制不同受教育水平人数条形图
plt.bar(range(5), height=[lv_0, lv_1, lv_2, lv_3, lv_4], width=0.4, alpha=0.8, color='skyblue')
plt.xticks([index for index in range(5)], ['未完成中学学历', '中学学历', '社区学院', '大学学位', '研究生学位'])
plt.xlabel('用户教育水平')
plt.ylabel('人数')
plt.title('受教育水平人数探索')
plt.show()


# 分类数据探索
label_list = ['是否结婚', '是否退休', '是否租借设备', '是否使用语音', '是否使用互联网', '是否支持电子凭证']  # 横坐标刻度显示值
hy0 = pd.value_counts(data['婚姻状况marital'])[0]
hy1 = pd.value_counts(data['婚姻状况marital'])[1]

tx0 = pd.value_counts(data['是否退休retire'])[0]
tx1 = pd.value_counts(data['是否退休retire'])[1]

zj0 = pd.value_counts(data['设备租赁equip'])[0]
zj1 = pd.value_counts(data['设备租赁equip'])[1]

yy0 = pd.value_counts(data['语音邮件voice'])[0]
yy1 = pd.value_counts(data['语音邮件voice'])[1]

hlw0 = pd.value_counts(data['互联网internet'])[0]
hlw1 = pd.value_counts(data['互联网internet'])[1]

dzpz0 = pd.value_counts(data['是否支持电子凭证ebill'])[0]
dzpz1 = pd.value_counts(data['是否支持电子凭证ebill'])[1]

True_list1 = [hy0, tx0, zj0, yy0, hlw0, dzpz0]  # 纵坐标值1
False_list2 = [hy1, tx1, zj1, yy1, hlw1, dzpz1]  # 纵坐标值2
x = range(len(True_list1))
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
rects1 = plt.bar(x, height=True_list1, width=0.4, alpha=0.8, color='red', label="是")
rects2 = plt.bar([i + 0.4 for i in x], height=False_list2, width=0.4, color='green', label="否")
plt.ylim(0, 500)  # y轴取值范围
plt.ylabel("人数")
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks([index + 0.2 for index in x], label_list)
plt.xlabel("分类情况")
plt.title("分类数据探索")
plt.legend()  # 设置题注
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 0.3, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 0.3, str(height), ha="center", va="bottom")
plt.show()


