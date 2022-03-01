# Majority voting의 앙상블 방법을 연습한다.
# ----------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report

# iris 데이터를 읽어온다.
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)

# 4가지 모델을 생성한다 (KNN, Decision tree, SVM, Logistic Regression).
# 각 모델은 최적 조건으로 생성한다. (knn의 k개수, dtree의 max_depth 등)
# sklearn 문서 : Recommended for an ensemble of well-calibrated classifiers.
knn = KNeighborsClassifier(n_neighbors=5, p=2)
dtree = DecisionTreeClassifier(criterion='gini', max_depth=8)
svm = SVC(kernel='rbf', gamma=0.1, C=1.0, probability=True)
lreg = LogisticRegression(max_iter=500)

# 4가지 모델로 앙상블을 구성한다.
base_model = [('knn', knn), ('dtree', dtree), ('svm', svm), ('lr', lreg)]
ensemble = VotingClassifier(estimators=base_model, voting='soft')

ensemble

# 4가지 모델을 각각 학습하고, 결과를 종합한다.
# VotingClassifier()의 voting = ('hard' or 'soft')에 따라 아래와 같이 종합한다.
# hard (default) : 4가지 모델에서 추정한 class = (0, 1, 2)중 가장 많은 것으로 판정.
# soft : 4가지 모델에서 추정한 각 class의 확률값의 평균 (혹은 합)을 계산한 후,
#        확률이 가장 높은 (argmax(P)) class로 판정한다.
ensemble.fit(x_train, y_train)

# 학습데이터와 시험데이터의 정확도를 측정한다.
print('\n학습데이터의 정확도 = %.2f' % ensemble.score(x_train, y_train))
print('시험데이터의 정확도 = %.2f' % ensemble.score(x_test, y_test))

# 시험데이터의 confusion matrix를 작성하고, (row : actual, col : predict),
# 4개 score를 확인한다.
y_pred = ensemble.predict(x_test)
print('\nConfusion matrix :')
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred, target_names=iris.target_names))


#bagging(bootstrap arregating)은 표본추출(랜덤)을 여러번하고 
# 각 각 1개의 모델링을 가지고 여러번 수행하고 종합한다.
# Bagging에 의한 앙상블 방법을 연습한다.
# ------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
import numpy as np
from sklearn.metrics import classification_report

# iris 데이터를 읽어온다.
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)

# 4가지 모델을 생성한다 (KNN, Decision tree, SVM, Logistic Regression).
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
dtree = DecisionTreeClassifier(criterion='gini', max_depth=8)
svm = SVC(kernel='rbf', gamma=0.1, C=1.0, probability=True)
lreg = LogisticRegression(max_iter=500)

# 4가지 모델로 Bagging을 구성하고, 각 모델의 추정 확률을 누적한다.
prob = np.zeros((y_test.shape[0], iris.target_names.shape[0]))
base_model = [knn, dtree, svm, lreg]
for m in base_model:
    bag = BaggingClassifier(base_estimator=m, n_estimators=100)
    bag.fit(x_train, y_train)
    
    prob += bag.predict_proba(x_test)

# 확률의 누적합이 가장 큰 class를 찾고, 정확도를 측정한다.
y_pred = np.argmax(prob, axis=1)

# 시험데이터의 confusion matrix를 작성한다 (row : actual, col : predict)
print('\nConfusion matrix :')
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred, target_names=iris.target_names))



# RandomForest에 의한 앙상블 방법을 연습한다. (결정트리에 이용)
# ------------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# iris 데이터를 읽어온다.
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)

rf = RandomForestClassifier(max_depth=3, n_estimators=100)
rf.fit(x_train, y_train)

# 시험데이터의 confusion matrix를 작성하고, (row : actual, col : predict),
# 4개 score를 확인한다.
y_pred = rf.predict(x_test)

print('\nConfusion matrix :')
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred, target_names=iris.target_names))




#boosting: 약한 학습기를 강한 학습기로 만드는 과정, 오차에 가중치를 더하고 맞춘것은
#가중치를 적게 하여 다시 학습을 진행함.


# AdaBoost에 의한 앙상블 방법을 연습한다.
# --------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# iris 데이터를 읽어온다.
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)

svm = SVC(kernel='rbf', gamma=0.1, C=1.0, probability=True)
aboost = AdaBoostClassifier(base_estimator=svm, n_estimators=100)
aboost.fit(x_train, y_train)

# 시험데이터의 confusion matrix를 작성하고, (row : actual, col : predict),
# 4개 score를 확인한다.
y_pred = aboost.predict(x_test)

print('\nConfusion matrix :')
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred, target_names=iris.target_names))
































