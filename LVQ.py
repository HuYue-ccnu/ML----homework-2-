# -*- coding:utf-8 -*-
import re
import math
import numpy as np
import pylab as pl
from fileRead import read_random_label

data, dataSet = read_random_label()
class watermelon:
    def __init__(self, properties):
        self.number = properties[0]
        self.density = float(properties[1])
        self.sweet = float(properties[2])
        self.good = properties[3]

#数据简单处理
a = re.split(',', data.strip(" "))

dataset = []     #dataset:数据集
for i in range(int(len(a)/4)):
    temp = tuple(a[i * 4: i * 4 + 4])
    dataset.append(watermelon(temp))
print("=====dataset=====")

#计算欧几里得距离,a,b分别为两个元组
def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

#算法模型
def LVQ(dataset, a, max_iter):
    #统计样本一共有多少个分类
    T = list(set(i.good for i in dataset))
    #随机产生原型向量
    P = [(i.density, i.sweet) for i in np.random.choice(dataset, len(T))]
    while max_iter > 0:
        X = np.random.choice(dataset, 1)[0]
        index = np.argmin(dist((X.density, X.sweet), i) for i in P)
        t = T[index]
        if t == X.good:
            P[index] = ((1 - a) * P[index][0] + a * X.density, (1 - a) * P[index][1] + a * X.sweet)
        else:
            P[index] = ((1 + a) * P[index][0] - a * X.density, (1 + a) * P[index][1] - a * X.sweet)
        max_iter -= 1
    return P

def train_show(dataset, P):
    
    C = [[] for i in P]
    print("**********")
    for i in dataset:
        if i.good == '1':
            C[0].append(i)
        elif i.good == '2':
            C[1].append(i)
        elif i.good == '3':
            C[2].append(i)
        else:
            C[3].append(i)

    return C

#画图
def draw(C, P):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(C)):
        coo_X = []    #x坐标列表
        coo_Y = []    #y坐标列表
        for j in range(len(C[i])):
            coo_X.append(C[i][j].density)
            coo_Y.append(C[i][j].sweet)
        pl.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)
    #展示原型向量
    P_x = []
    P_y = []
    for i in range(len(P)):
        P_x.append(P[i][0])
        P_y.append(P[i][1])
        pl.scatter(P[i][0], P[i][1], marker='o', color=colValue[i%len(colValue)], label="vector")
    pl.legend(loc='upper right')
    pl.show()

P = LVQ(dataset, 0.00001, 5000)
C = train_show(dataset, P)
draw(C, P)
