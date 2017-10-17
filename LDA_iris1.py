import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


# 读取iris数据，
# 这个数据的特征维度为4维
# 样本的类别有三种
iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names

# 将数据的特征维度降为一维
# 当然这里可以将n_components设置为任何小于原始特征维度的数目
lda = LinearDiscriminantAnalysis(n_components=1)
X_r2 = lda.fit(X, y).transform(X)
print(X_r2)
X_Zreo = np.zeros(X_r2.shape)

for c ,i , target_names in zip('ryb', [0, 1, 2], target_names):#zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
    plt.scatter(X_r2[y == i], X_Zreo[y == i], c=c, label=target_names)

plt.grid()
plt.legend()
plt.show()