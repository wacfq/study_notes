
from sklearn import svm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

# 数据读取
datafile = '../data/cleaned_data.csv'  # 原始数据,第一行为属性标签
data = pd.read_csv(datafile, encoding='utf-8')
# data = np.array(data)

# 抽取30%的数据作为测试集，其余为训练集
train, test = train_test_split(data, test_size=0.3)


train_x = data.iloc[:, 0:29]         # 这里只是选取部分特征作为主要特征去分类
train_y = data['是否流失churn']
test_x = data.iloc[:, 0:29]
test_y = data['是否流失churn']

# 对数据进行Z-score规范化，避免因为数据量级不同而导致的权重不同（数据转换）
ss = preprocessing.StandardScaler()
train_xx = ss.fit_transform(train_x)
test_xx = ss.transform(test_x)

# train_x.shape, test_x.shape(398, 6)(171, 6)
# print(train_x)

# 创建SVM 分类器
model = svm.SVC()
# 用训练集做训练
model.fit(train_x, train_y)
# 预测测试集
prediction = model.predict(test_x)

# 计算预测的准确率
print("预测的准确率是：", accuracy_score(prediction, test_y))

print(prediction)
print(test_y)
