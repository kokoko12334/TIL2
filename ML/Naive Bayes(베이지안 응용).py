#p(y|x)=p(x|y)p(y)/p(x)를 이용하고 
#과거 데이터를 이용하여 다음 식을 가정하고,
#다음 x조건일 때 y의 확률을 계산하는데, 이때 가장 높은 확률을 선택함


# Naive Bayes로 iris 데이터를 학습한다.
# feature들이 모두 실숫값이므로 gaussian model을 사용한다.
# ------------------------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# iris data set을 읽어온다
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = \
    train_test_split(iris.data, iris.target, test_size = 0.2)

# Gaussian model로 Train 데이터 세트를 학습한다.
model = GaussianNB()
model.fit(x_train, y_train)

print("\n* Gaussian model :")
print("* 학습용 데이터로 측정한 정확도 = %.2f" % model.score(x_train, y_train))
print("* 시험용 데이터로 측정한 정확도 = %.2f" % model.score(x_test, y_test))

########수입 데이터 분석
# Naive Bayes 분류기로 income 데이터 세트를 학습한다.
# categorical과 gaussian feature가 섞여 있는 경우, 각 feature를 분리하여 MultinomialNB와
# GaussianNB로 나눠서 학습하고 추정 확률을 곱한 값으로 시험 데이터의 label을 추정한다.
# ------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB

# income 데이터를 읽어온다
# https://www.kaggle.com/wenruliu/adult-income-dataset?select=adult.csv


income = pd.read_csv('adult.csv')
income.head()

# categorical feature를 숫자로 변환한다.
cat_features = [i for i in income.columns if income[i].dtype=='O']

income.columns.dtype
type(income.columns[0])
for c in cat_features:
    income[c] = pd.Categorical(income[c]).codes

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x = np.array(income)[:, :-1]
y = np.array(income)[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# categorical feature를 multinomial naive bayes로 학습한다.
# --------------------------------------------------------
cat_n = [1, 3, 4, 5, 6, 7, 9]
catx_train = x_train[:, cat_n]
catx_test = x_test[:, cat_n]

# Multinomial model로 categorical Train 데이터 세트를 학습한다.
model_m = MultinomialNB(alpha=1.0)  # alpha = 1.0 : Laplace smoothing (default)
model_m.fit(catx_train, y_train)

# gaussian feature를 gaussian naive bayes로 학습한다.
# --------------------------------------------------
gau_n = [0, 2, 8]
gaux_train = x_train[:, gau_n]
gaux_test = x_test[:, gau_n]

# Gaussian model로 gaussian Train 데이터 세트를 학습한다.
model_g = GaussianNB()
model_g.fit(gaux_train, y_train)

# 시험 데이터를 이용하여 정확도를 측정한다. 시험데이터도 categorical과 gaussian으로
# 분리돼 있다. 각각의 모형에 따라 확률을 추정한다.
cat_prob = model_m.predict_proba(catx_test)
gau_prob = model_g.predict_proba(gaux_test)

# 두 확률을 곱한다.
mix_prob = np.multiply(cat_prob, gau_prob)

# 두 확률의 곱으로 정확도를 측정한다.
mix_label = np.argmax(mix_prob, 1)
accuracy = (y_test == mix_label).mean()

print("\n* 시험용 데이터로 측정한 정확도 = %.2f" % accuracy)

















































