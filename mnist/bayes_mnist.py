#encoding=utf-8

import pandas as pd
import numpy as np
import cv2
import time

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 二值化，有图像的位置255像素值转换成0，其他位置转换成1
def binaryzation(img):
    cv_img = img.astype(np.uint8)
    cv2.threshold(cv_img,50,1,cv2.THRESH_BINARY_INV,cv_img)
    return cv_img

def Train(trainset,train_labels):
    prior_probability = np.zeros(class_num)                         # 先验概率
    conditional_probability = np.zeros((class_num,feature_len,2))   # 条件概率

    # 计算先验概率及条件概率
    for i in range(len(train_labels)):
        img = binaryzation(trainset[i])     # 图片二值化
        label = train_labels[i]

        prior_probability[label] += 1#标签为x的个数

        for j in range(feature_len):#784列矩阵，每个像素点处是个二维[,]元素，有图像的位置在第一个位置，没图像的像素点在第二个位置
            conditional_probability[label][j][img[j]] += 1#同一个标签每个像素点处有图像的点加总

    # 将概率归到[1.10001]
    for i in range(class_num):
        for j in range(feature_len):

            # 经过二值化后图像只有0，1两种取值
            pix_0 = conditional_probability[i][j][0]#有图像的点
            pix_1 = conditional_probability[i][j][1]#没有图像的点
            # 计算0，1像素点对应的条件概率  每个像素点有图像的概率
            probalility_0 = (float(pix_0)/float(pix_0+pix_1))*1000000 + 1
            probalility_1 = (float(pix_1)/float(pix_0+pix_1))*1000000 + 1

            conditional_probability[i][j][0] = probalility_0
            conditional_probability[i][j][1] = probalility_1

    return prior_probability,conditional_probability

# 计算概率
def calculate_probability(img,label):
    probability = int(prior_probability[label])

    for i in range(len(img)):
        probability *= int(conditional_probability[label][i][img[i]])#独立分量概率相乘 分子部分 对于先验概率都要除以10 结果一样直接用的计数 每个分量又有是否有图像的两种状态

    return probability

def Predict(testset,prior_probability,conditional_probability):
    predict = []

    for img in testset:

        # 图像二值化
        img = binaryzation(img)

        max_label = 0
        max_probability = calculate_probability(img,0)

        for j in range(1,10):
            probability = calculate_probability(img,j)

            if max_probability < probability:
                max_label = j
                max_probability = probability

        predict.append(max_label)

    return np.array(predict)


class_num = 10
feature_len = 784

if __name__ == '__main__':

    print ('Start read data')

    time_1 = time.time()

    raw_data = pd.read_csv('Mnist_data/train.csv',header=0)#从第一行开始读取
    data = raw_data.values#由每个训练图片对应的784个像素点矩阵

    imgs = data[0::,1::]#去掉标签列
    labels = data[::,0]#第一列为标签列

    # 选取 2/3 数据作为训练集， 1/3 数据作为测试集，由sklearn包提供分集功能
    train_features, test_features, train_labels, test_labels = train_test_split(imgs, labels, test_size=0.33, random_state=23323)
    # print train_features.shape
    # print train_features.shape

    time_2 = time.time()
    print ('read data cost ',time_2 - time_1,' second','\n')

    print ('Start training')
    prior_probability,conditional_probability = Train(train_features,train_labels)
    time_3 = time.time()
    print ('training cost ',time_3 - time_2,' second','\n')

    print ('Start predicting')
    test_predict = Predict(test_features,prior_probability,conditional_probability)
    time_4 = time.time()
    print ('predicting cost ',time_4 - time_3,' second','\n')

    score = accuracy_score(test_labels,test_predict)
    print ("The accruacy socre is ", score)