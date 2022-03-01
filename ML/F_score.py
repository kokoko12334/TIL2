from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ROC AUC score 연습 코드
# ----------------------
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

# 학습 데이터를 읽어온다.
cancer = load_breast_cancer()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(cancer['data'], cancer['target'], test_size = 0.2)

# KNN 으로 Train 데이터 세트를 학습한다.
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

# Test 세트의 Feature에 대한 class를 추정하고, 정확도를 계산한다
y_pred = knn.predict_proba(x_test)[:, 1]

# ROC curve를 그린다
fprs, tprs, thresholds = roc_curve(y_test, y_pred)

# thresholdsndarray of shape = (n_thresholds,)
# Decreasing thresholds on the decision function used to compute fpr and tpr. 
# thresholds[0] represents no instances being predicted and is arbitrarily set to max(y_score) + 1.
# y_pred = 1.0인 경우도 있을 수 있으므로 가장 큰 threshold는 1.0보다 크게 적용한 것 같음.

plt.plot(fprs, tprs, marker= 'o', label = 'ROC')
plt.plot([0,1], [0,1], '--', label = 'Random')
plt.legend()
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()

# AUC (Area Under Curve)를 계산한다
auc = roc_auc_score(y_test, y_pred)
print("ROC AUC = {0:.4f}".format(auc))






#iris(다중 클래스)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
iris = load_iris()

iris_x = iris.data
iris_y = iris.target
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.2)
###knn
from sklearn.neighbors import KNeighborsClassifier


knn =KNeighborsClassifier()
knn.get_params()
params ={'n_neighbors': range(1,11)}
grid = GridSearchCV(estimator=knn, param_grid=params, cv=5, refit=True)     
grid.fit(x_train, y_train)
y_pred = grid.predict(x_test)

print(' Accuracy = %.3f' % accuracy_score(y_test, y_pred))
print('   Recall = %.3f' % recall_score(y_test, y_pred, average='macro'))
print('Precision = %.3f' % precision_score(y_test, y_pred, average='macro'))
print(' F1-score = %.3f' % f1_score(y_test, y_pred, average='macro'))
# AUC (Area Under Curve)를 계산한다
auc = roc_auc_score(y_test, y_pred)
print("ROC AUC = {0:.4f}".format(auc))

#0중심
y_test0 = [1 if i==0 else 0 for i in y_test]
fprs, tprs, thresholds = roc_curve(y_test0, y_pred[:,0])
plt.plot(fprs, tprs, label = 'ROC')
plt.plot([0,1], [0,1], '--', label = 'Random')
plt.legend()
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()
#1중심
y_test1= [1 if i==1 else 0 for i in y_test]

fprs, tprs, thresholds = roc_curve(y_test1, y_pred[:,1])

plt.plot(fprs, tprs, label = 'ROC')
plt.plot([0,1], [0,1], '--', label = 'Random')
plt.legend()
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()
#2중심
y_test2 = [1 if i==2 else 0 for i in y_test]

fprs, tprs, thresholds = roc_curve(y_test2, y_pred[:,2])

plt.plot(fprs, tprs, label = 'ROC')
plt.plot([0,1], [0,1], '--', label = 'Random')
plt.legend()
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()

# AUC (Area Under Curve)를 계산한다
auc = roc_auc_score(y_test0, y_pred[:,0])
print("ROC AUC = {0:.4f}".format(auc))


##dt
from sklearn.tree import DecisionTreeClassifier

##svc
from sklearn.svm import SVC





























