from sklearn import svm
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import sklearn
from sklearn.model_selection import train_test_split


# 数据读取
datafile = '../data/cleaned_data.csv'  # 原始数据,第一行为属性标签
data = pd.read_csv(datafile, encoding='utf-8')
data = np.array(data)
# X = data.iloc[:, 0:29]
# y = data['是否流失churn']

# 2.划分数据与标签
x, y = np.split(data, indices_or_sections=(29,), axis=1)    # x为数据，y为标签

# x = x[:, 0:2]    # 为便于后边画图显示，只选取前两维度。若不用画图，可选取前四列x[:,0:4]
train_data, test_data, train_label, test_label = sklearn.model_selection.train_test_split(x, y, random_state=1,
                                                                                         train_size=0.6, test_size=0.4)

# 3.训练svm分类器
classifier = svm.SVC(C=500, kernel='rbf', gamma=50, decision_function_shape='ovo')     # ovr:一对多策略
classifier.fit(train_data, train_label.ravel())        # ravel函数在降维时默认是行序优先

# 4.计算svc分类器的准确率
print("训练集：", classifier.score(train_data, train_label))
print("测试集：", classifier.score(test_data, test_label))


# # 查看决策函数
# print('train_decision_function:\n', classifier.decision_function(train_data))  # (90,3)
# print('predict_result:\n', classifier.predict(train_data))

