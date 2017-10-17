#coding:utf-8
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
iris = datasets.load_iris()
trains = iris.data[:120]
tests = iris.data[120:]
trains_label = iris.target[:120]
tests_label = iris.target[120:]
print('first 10 raw samples:', trains[:10])
clf = LinearDiscriminantAnalysis(n_components=1)
clf.fit(trains, trains_label)
trains_r = clf.transform(trains)
pre_label = clf.predict(tests)

#降维结果
print ('first 10 transformed samples:', trains_r[:10])
#预测目标分类结果
print ('predict value:', pre_label)
print('tests_label:',tests_label)
score = accuracy_score(tests_label,pre_label)
print ("The accruacy socre is ", score)