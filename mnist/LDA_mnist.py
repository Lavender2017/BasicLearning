#coding:utf-8
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
raw_data = pd.read_csv('Mnist_data/train.csv',header=0)#从第一行开始读取
data = raw_data.values#由每个训练图片对应的784个像素点矩阵
imgs = data[0::,1::]#去掉标签列
labels = data[::,0]#第一列为标签列

# 选取 2/3 数据作为训练集， 1/3 数据作为测试集，由sklearn包提供分集功能
train_features, test_features, train_labels, test_labels = train_test_split(imgs, labels, test_size=0.33, random_state=23323)
clf = LinearDiscriminantAnalysis(n_components=1)
clf.fit(train_features, train_labels)
trains_r = clf.transform(train_features)
pre_label = clf.predict(test_features)

#降维结果
print ('first 10 transformed samples:', trains_r[:10])
#预测目标分类结果
print ('predict value:', pre_label[:20])
print('tests_label:',test_labels[:20])
score = accuracy_score(test_labels,pre_label)
print ("The accruacy socre is ", score)