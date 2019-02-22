# -*- coding: utf-8 -*-

import numpy as np
import random
import codecs
import re
import matplotlib.pyplot as plt
from fileRead import read_random_label

def calcuDistance(vec1,vec2):
    #向量之间的欧式距离
    return np.sqrt(np.sum(np.square(vec1-vec2)))

def loadDataSet(path):
    data = codecs.open(path,'r','utf-8').readlines()
    dataSet = list()
    for line in data:
        line = line.strip()
        strList = re.split('[ ]+',line)
        
        numList = list()
        for item in strList:
            num = float(item)
            numList.append(num)
        dataSet.append(numList)
    return dataSet

#Data = loadDataSet('data/2_1.txt')
#print(Data)
def initCentroids(dataSet,k):
    #初始化K个质心，随机获取
    return random.sample(dataSet,k)

def minDistance(dataSet,centroidList):
    
    clusterDict = dict() #保存簇类结果
    for item in dataSet:
        vec1 = np.array(item)
        flag = 0              #簇分类标记
        minDis = float("inf") #初始化为最大值
        
        for i in range(len(centroidList)):
            vec2 = np.array(centroidList[i])
            distance = calcuDistance(vec1,vec2)
            if distance < minDis:
                minDis = distance
                flag = i
                
        if flag not in clusterDict.keys():  #簇族标记不存在，进行初始化
            clusterDict[flag] = list()
        clusterDict[flag].append(item)  #加入相应的类别中
    return clusterDict   #新的聚类结果

def getCentroids(clusterDict):
    #得到K个质心
    centroidList = list()
    for key in clusterDict.keys():
        centroid = np.mean(np.array(clusterDict[key]),axis=0) #计算每列的均值，即找到质心
        centroidList.append(centroid)
    return np.array(centroidList).tolist()

def getVar(clusterDict,centroidList):
    #计算簇集合间的均方误差
    #将簇类中各个向量与质心的距离进行累加求和
     sum_ = 0.0
     for key in clusterDict.keys():
         vec1 = np.array(centroidList[key])
         distance = 0.0
         for item in clusterDict[key]:
             vec2 = np.array(item)
             distance += calcuDistance(vec1,vec2)
         sum_ += distance
     return sum_
def showCluster(centroidList,clusterDict):
    
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow'] #不同簇类的标记
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw'] #质心标记
    for key in clusterDict.keys():
        plt.plot(centroidList[key][0],centroidList[key][1],centroidMark[key],markersize=12) #画质心点
        for item in clusterDict[key]:
            plt.plot(item[0],item[1],colorMark[key]) #画簇类下的点
    plt.show()
    
if __name__ == '__main__':
    path = "data/HW2_cluster/clusterTestData.txt"
    data_LVQ, dataSet = read_random_label()
    centroidList = initCentroids(dataSet, 4)
    
    clusterDict = minDistance(dataSet,centroidList) #第一次聚类迭代
    newVar = getVar(clusterDict,centroidList) #获得均方误差值，通过新旧均方误差来获得迭代终止条件
    oldVar = -0.0001
    print("===========第1次迭代===========")
#    print("簇类")
#    for key in clusterDict.keys():
#        print(key,"-->",clusterDict[key])
#    print("k个均值向量：",centroidList)
#    print("平均均方误差：",newVar)
    showCluster(centroidList,clusterDict)
    
    k = 2
    while abs(newVar-oldVar) >= 0.0001:
        #连续两次聚类结果小于0.0001时，迭代中止
        centroidList = getCentroids(clusterDict)  #获得新的质心、
        clusterDict = minDistance(dataSet,centroidList) #获得新的聚类结果
        oldVar = newVar
        newVar = getVar(clusterDict,centroidList)
        print("==========第%d次迭代=========="%k)
#        print("簇类")
#        for key in clusterDict.keys():
#            print(key,"-->",clusterDict[key])
#        print("k个均值向量：",centroidList)
#        print("平均均方误差：",newVar)
        showCluster(centroidList,clusterDict)
            
        k+=1
            
    
    
            