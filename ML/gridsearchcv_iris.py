# -*- coding: utf-8 -*-
"""GridSearchCV(iris).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ePwb-4QxGF-xo4aL1sQAvcmFT2xiM3nE
"""

# GridSearchCV cross validation 기능 연습
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
#DT
iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)
#refit은 최적 파라미터로 맞추어라
dt_params = [{'max_depth': np.arange(1, 20)}]
dt = DecisionTreeClassifier()
grid = GridSearchCV(estimator=dt, param_grid=dt_params, cv=5, refit=True)     
grid.fit(x_train, y_train)

grid.cv_results_
grid.cv_results_.keys()

grid.best_params_
grid.best_estimator_
# grid.cv_results_     : K-fold cross validation test 결과 dictionary
# grid.best_params_    : best parameter ==> {'max_depth': 5}
# grid.best_estimator_ : best parameter로 생성한 tree

# 최적 모델로 시험 데이터의 성능을 평가한다.
#굳이 이렇게 지정안하고 grid만 쓰면됨.
best_model = grid.best_estimator_

print("\n최적 파라메터 =", grid.best_params_)
print("시험 데이터 정확도 = {:.4f}".format(grid.score(x_test, y_test)))
print("시험 데이터 정확도 = {:.4f}".format(best_model.score(x_test, y_test)))



#SVM
from sklearn.svm import SVC
import mglearn
import numpy as np
import pandas as pd

model = SVC(kernel='rbf')

model.get_params().keys()         #파라미터 명을 정확히 알 수 있음.

para = {'gamma':range(0,10), 'C':range(0,5)}
grid = GridSearchCV(estimator= model, param_grid =para, cv=5, refit = True )


grid.fit(x_train, y_train)

print("\n최적 파라메터 =", grid.best_params_)
print("시험 데이터 정확도 = {:.4f}".format(grid.score(x_test, y_test)))










