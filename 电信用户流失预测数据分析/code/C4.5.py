import math
import operator
import pandas as pd
import numpy as np
import draw_tree as dw
from sklearn.model_selection import train_test_split


# 计算数据的信息熵
def calcEntropy(data):
    numSamples = len(data)
    numClass = {}
    Entropy = 0.0
    label = [sample[-1] for sample in data]
    for i in label:
        numClass[i] = numClass.get(i, 0)+1   # 求不同类的数量
    for j in numClass:
        prob = float(numClass[j]/numSamples)
        Entropy = Entropy - prob*math.log(prob,2)
    return Entropy


# 取出数据中第i列值为setValue的样本
def splitData(data,i,setValue):
    subData = []
    for sample in data:
        if sample[i] == setValue:
            reducedSample = sample[:i]    # 删除该样本的第i列
            reducedSample.extend(sample[i+1:])
            subData.append(reducedSample)
    return subData


# 选择最优属性
def slctAttribute(data):
    allEntropy = calcEntropy(data)
    numSamples = len(data)
    numAttributes = len(data[0])-1
    initMI = 0.0
    for i in range(numAttributes):
        valueList = [sample[i] for sample in data]  # 拿出数据的第i列
        value = set(valueList)  # 拿出这一列的所有不等值
        numEntropy = 0.0
        for j in value:
            subData = splitData(data, i, j)
            proportion = float(len(subData)/numSamples)
            Entropy = calcEntropy(subData)
            numEntropy = numEntropy + Entropy*proportion
        MI = allEntropy - numEntropy    # 计算互信息
        if MI > initMI:
            initMI = MI
            slcAttribute = i
    return slcAttribute


# 属性已遍历到最后一个，取该属性下样本最多的类为叶节点类别标记
def majorVote(classList):
    classCount = {}
    for i in classList:
        # 第一次进入，分别把classList的不同值赋给classCount的键值
        if i not in classCount.keys():
            # 构建键值对，用于对每个classList的不同元素来计数
            classCount[i] = 0
        else:
            classCount[i] += 1
    # 按每个键的键值降序排列
    sortClassCount = sorted(classCount.items, key=operator.itemgetter(1), reverse=True)
    return sortClassCount[0][0]


def createTree(data,attributes):
    classList = [i[-1] for i in data]   # 取data的最后一列（标签值）
    # count出classList中第一个元素的数目，如果和元素总数相等，那么说明样本全部属于某一类，此时结束迭代
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(data[0]) == 1:      # 遍历后只剩下一个属性，那么标记类别为样本最多的类
        return majorVote(classList)
    selectAttribute = slctAttribute(data)
    bestAttribute = attributes[selectAttribute]
    myTree = {bestAttribute:{}}       # 生成树，采用字典嵌套的方式记录树
    del(attributes[selectAttribute])    # 删除此时的最优属性
    attributeValue = [sample[selectAttribute] for sample in data]        # 取出data所有样本的第selectAttribute个变量的值
    branch = set(attributeValue)    # 取唯一取值，作为本节点的所有分支
    for value in branch:
        subAttributes = attributes[:]
        myTree[bestAttribute][value] = createTree(splitData(data, selectAttribute, value), subAttributes)  # 迭代生成子树
    return myTree


if __name__ == '__main__':

    datafile = '../data/决策树.csv'  # 原始数据,第一行为属性标签
    data = pd.read_csv(datafile, encoding='utf-8')
    # print(data)

    # 抽取30%的数据作为测试集，其余为训练集
    train, test = train_test_split(data, test_size=0.3)
    print(train)

    # 首先将pandas读取的数据转化为array
    data_array = np.array(train)
    # 然后转化为list形式
    data_list = data_array.tolist()

    attributes = data.columns.tolist()
    attributes.pop(-1)

    print(attributes)

    Tree = createTree(data_list, attributes)
    print(Tree)
    # dw.createPlot(Tree)




