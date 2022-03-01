from itertools import groupby
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#데이터 불러오고 확인하기
data=pd.read_csv('diabetes.csv' , sep=",")
data.head()
target = data.pop('Outcome')

#train, test data로 분류하기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)


#KNN사용하기
from sklearn.neighbors import KNeighborsClassifier

lst = []
for k in range(1,21):
    knn = KNeighborsClassifier(n_neighbors = k, weights='distance')    
    knn.fit(x_train, y_train)
    lst.append(knn.score(x_test, y_test))

print(f'KNN score:{max(lst)}, k:{lst.index(max(lst))+1}')

#예측하기
new = np.array([[3,127,85,25,473,27,0.5,39]])
knn = KNeighborsClassifier(n_neighbors = lst.index(max(lst))+1, weights='distance')
knn.fit(x_train, y_train)
print(f'예측값: {knn.predict(new)}')



#Decision Tree 사용하기
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

lst = []
for k in range(1,21):
    clf = DecisionTreeClassifier(max_depth=k)    
    clf.fit(x_train, y_train)
    lst.append(clf.score(x_test, y_test))

print(f'Decision Tree score:{max(lst)}, k:{lst.index(max(lst))+1}')

#예측하기
new = np.array([[3,127,85,25,473,27,0.5,39]])
clf = DecisionTreeClassifier(max_depth=lst.index(max(lst))+1)
clf.fit(x_train, y_train)
print(f'예측값: {clf.predict(new)}')














#########변수별 상관계수 행렬
import seaborn as sns

df_corr = data.corr(method='pearson')
plt.figure(figsize=(8, 6))
sns.heatmap(df_corr, annot=True)
plt.show()

