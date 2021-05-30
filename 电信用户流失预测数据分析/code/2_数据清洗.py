#-*- coding: utf-8 -*-



# 处理缺失值与异常值

import numpy as np
import pandas as pd

datafile = '../data/data.csv'  # 原始数据路径
cleanedfile = '../data/cleaned_data.csv'  # 数据清洗后保存的文件路径

# 读取数据
data = pd.read_csv(datafile, encoding='utf-8')
# data = pd.DataFrame(data)
print('原始数据的形状为：', data.shape)
# print(data)

# # 将定性数据量化
# 婚姻情况
data.loc[data['婚姻状况marital'] == '未婚', '婚姻状况marital'] = 0
data.loc[data['婚姻状况marital'] == '已婚', '婚姻状况marital'] = 1

# 婚姻情况
data.loc[data['性别gender'] == '女', '性别gender'] = 0
data.loc[data['性别gender'] == '男', '性别gender'] = 1

# 受教育水平
data.loc[data['受教育水平ed'] == '未完成中学学历', '受教育水平ed'] = 0
data.loc[data['受教育水平ed'] == '中学学历', '受教育水平ed'] = 1
data.loc[data['受教育水平ed'] == '社区学院', '受教育水平ed'] = 2
data.loc[data['受教育水平ed'] == '大学学位', '受教育水平ed'] = 3
data.loc[data['受教育水平ed'] == '研究生学位', '受教育水平ed'] = 4

# 客户类别
data.loc[data['客户类别custcat'] == '基础服务', '客户类别custcat'] = 0
data.loc[data['客户类别custcat'] == '电子服务', '客户类别custcat'] = 1
data.loc[data['客户类别custcat'] == '附加服务', '客户类别custcat'] = 2
data.loc[data['客户类别custcat'] == '总服务', '客户类别custcat'] = 3

# 将所有的“是”或”否“量化
for i in data:
    # print(i)
    data.loc[data[i] == '否', i] = 0
    data.loc[data[i] == '是', i] = 1


# 去除数据中有空值的行数
new_data = data.dropna()
print('删除缺失记录后数据的形状为：', new_data.shape)
print(new_data)

# 保存清洗后的数据
new_data.iloc[:, 1:].to_csv(cleanedfile, index=False)

