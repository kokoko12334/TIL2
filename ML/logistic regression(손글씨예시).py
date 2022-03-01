# Logistic Regression으로 diabates 데이터를 학습한다.
# binary classification (class = [0, 1])
# ------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# diabetes 데이터를 읽어온다
# DATA_PATH = '/content/drive/MyDrive/Colab Notebooks/data/'
data = pd.read_csv('diabetes.csv')

f_data = np.array(data.drop('Outcome', axis=1))
t_data = np.array(data['Outcome'])
data.head()

# 데이터를 표준화한다. train과 test 데이터를 동시에 표준화 했다.
# 괜찮을까? 문제라면 무엇이 문제일까?
f_scale = StandardScaler()
t_scale = StandardScaler()

f_scaled = f_scale.fit_transform(f_data)

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(f_scaled, t_data, test_size = 0.2)

# Logistic Regression으로 Train 데이터 세트를 학습한다.
model = LogisticRegression()
model.fit(x_train, y_train)

# Test 세트의 Feature에 대한 class를 추정하고, 정확도를 계산한다
print("* 학습용 데이터로 측정한 정확도 = %.2f" % model.score(x_train, y_train))
print("* 시험용 데이터로 측정한 정확도 = %.2f" % model.score(x_test, y_test))

# 학습된 w, b를 확인해 본다.
print('\nw :')
print(model.coef_)
print('\nb :')
print(model.intercept_)
print('\nclass :')
print(model.classes_)

# x_test[n]의 class를 추정한다.
n = 1
y_pred = model.predict(x_test[n].reshape(1, -1))[0]
print('y_test[{}] = {}, y_pred = {}'.format(n, y_test[n], y_pred))
print('probability = ', model.predict_proba(x_test[n].reshape(1, -1))[0])
#1일 확률이 0.1111, 0일 확률이 0.88888

# manual로 x_test[n]의 class를 추정해 본다. 각 파라메터의 기능을 확인한다.
theta = np.dot(model.coef_[0], x_test[n]) + model.intercept_
prob = 1.0 / (1.0 + np.exp(-theta))
print('probability = ', prob)



##############mnist
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

DATA_PATH = 'C:/Users/user/Desktop/git/TIL/'

mnist = fetch_openml('mnist_784')
with open(DATA_PATH + 'mnist.pkl', 'wb') as f:
       pickle.dump(mnist, f)

# 저장된 mnist 데이터를 읽어온다.
with open(DATA_PATH + 'mnist.pkl', 'rb') as f:
        mnist = pickle.load(f)

print(mnist.keys())

type(mnist['data'])

# 데이터가 많아 시간이 오래걸리므로, 앞 부분 10000개만 분석한다.
x_feat = np.array(mnist['data'][:10000])
y_target = np.array(mnist['target'][:10000])

# n-번째 손글씨 이미지를 확인해 본다.
n = 10
img = x_feat[n].reshape(28,28)
print('\nclass =', y_target[n])
plt.imshow(img)
plt.show()

############gridsearch
x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size = 0.2)
params = [{'C': [0.1, 0.5, 1.0]}]
model = LogisticRegression(penalty='l2', max_iter=500)
grid = GridSearchCV(estimator=model, param_grid=params, cv=5, refit=True)
grid.fit(x_train, y_train)

# 최적 모델로 시험 데이터의 성능을 평가한다.
best_model = grid.best_estimator_

print("\n최적 파라메터 =", grid.best_params_)
print("시험 데이터 정확도 = {:.4f}".format(best_model.score(x_test, y_test)))

# 잘못 분류한 이미지 몇개를 확인해 본다.
# 어떤 이미지를 잘 맞추지 못할까? 사람이라면 아래 이미지를 잘 맞출 수 있을까?
y_pred = best_model.predict(x_test)

n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(12,4))
for i, miss in enumerate(miss_sam):
    x = x_test[miss] * 255  # 표준화 단계에서 255로 나누었으므로, 여기서는 곱해준다.
    x = x.reshape(28, 28)   # 이미지 확인을 위해 (28 x 28) 형태로 변환한다.
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_test[miss]) + ' / ' + str(y_pred[miss]))







#############################################


from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
# x_feat = x_feat[:1001]
# y_target = y_target[:1001]

####KNN

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
print("knn = {:.4f}".format(knn.score(x_test, y_test)))

knn.get_params().keys()
para = {'n_neighbors' : range(1,6)} 
knn_grid = GridSearchCV(estimator=knn, param_grid= para, cv = 5, refit = True)
knn_grid.fit(x_feat, y_target)
print("\n최적 파라메터 =", knn_grid.best_params_)
print("시험 데이터 정확도 = {:.4f}".format(knn_grid.score(x_feat, y_target)))

####DT
dt = DecisionTreeClassifier(max_depth = 5)
dt.fit(x_train, y_train)
dt.score(x_train, y_train)
dt.score(x_test, y_test)

#####SVC
svc = SVC(kernel='rbf')
svc.fit(x_train, y_train)
print("svc= {:.4f}".format(svc.score(x_test, y_test)))
y_pred = svc.predict(x_test)

n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(12,4))
for i, miss in enumerate(miss_sam):
    x = x_test[miss] * 255  # 표준화 단계에서 255로 나누었으므로, 여기서는 곱해준다.
    x = x.reshape(28, 28)   # 이미지 확인을 위해 (28 x 28) 형태로 변환한다.
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_test[miss]) + ' / ' + str(y_pred[miss]))


svc.get_params().keys()         
para = {'gamma':range(1,5), 'C':range(1,2)}
svc_grid = GridSearchCV(estimator= svc, param_grid =para, cv=5, refit = True )
svc_grid.fit(x_feat, y_target)

print("\n최적 파라메터 =", svc_grid.best_params_)
print("시험 데이터 정확도 = {:.4f}".format(svc_grid.score(x_feat, y_target)))

####LogisticRegression

logic = LogisticRegression()
logic.fit(x_train, y_train)
print("logic = {:.4f}".format(logic.score(x_test, y_test)))


