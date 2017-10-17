import numpy as np
import matplotlib.pyplot as plt

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix = np.mat(dataMatIn)#列表转换成矩阵
    # print(dataMatrix)
    labelMat = np.mat(classLabels).transpose()
    # print(labelMat)
    m,n = np.shape(dataMatrix)
    alpha = 0.001#向目标移动的步长
    maxCycles = 500#迭代次数
    weights = np.ones((n,1))
    # print(weights)
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)#计算出来的函数值对应的列向量
        # print(h)
        error = (labelMat-h)
        weights = weights+alpha*dataMatrix.transpose()*error
    return weights

def plotBestFit(wei,dataMat, labelMat):
    weights = wei.getA() #将矩阵wei转化为list
    dataArr = np.array(dataMat)#将列表转换成数组
    print(dataArr)
    n = np.shape(dataArr)[0]#样本数
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])#dataArr[i, 1]第i行2列
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    #首先我们得到了最后分类函数 y=θ0+θ1x1+θ2x2我们画出y=0这条直线 x1在-3到3直接相差为1的值则x2=（-θ0-θ1x1）/θ2
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
dataMat,labelMat = loadDataSet()
weights = gradAscent(dataMat,labelMat)
plotBestFit(weights,dataMat,labelMat)

