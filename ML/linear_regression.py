
# 1차원 데이터로 Linear Regression 기능을 연습한다.
# ------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
from sklearn.linear_model import LinearRegression

# 샘플 데이터 1,000개를 생성한다
# y = ax + b + e
def createData(a, b, n):
   resultX = []
   resultY = []
   for i in range(n):
       x = np.random.normal(0.0, 0.5)
       y = a * x + b + np.random.normal(0.0, 0.05)
       resultX.append(x)
       resultY.append(y)
       
   return np.array(resultX).reshape(-1,1), np.array(resultY).reshape(-1,1)

# Train 데이터 세트를 구성한다
X, Y = createData(0.1, 0.3, 1000) # y = 0.1x + 0.3 + e

fig = plt.figure(figsize=(5, 5))
plt.plot(X, Y, 'ro', markersize=1.5)
plt.show()

# Linear Regression으로 Train 데이터 세트를 학습한다.
model = LinearRegression()
model.fit(X, Y)

# 결과를 확인한다
a = model.coef_[0][0]
b = model.intercept_[0]
print("\n* 회귀직선의 방정식 (OLS) : y = %.4f * x +  %.4f" % (a, b))
yHat =  model.predict(X)

fig = plt.figure(figsize=(5, 5))
plt.plot(X, Y, 'ro', markersize=1.5)
plt.plot(X, yHat)
plt.show()

# 시험 데이터 전체의 오류를 R-square로 표시한다.
print('\n시험 데이터 전체 오류 (R2-score) = %.4f' % model.score(X, Y))

# R-square를 manual로 계산하고, model.score() 결과와 비교한다.
# SSE : explained sum of square
# SSR : residual sum of square (not explained)
# SST : total sum of square
# R-square : SSE / SST or 1 - (SSR / SST)
ssr = np.sum(np.square(Y - yHat))
sst = np.sum(np.square(Y - Y.mean()))
R2 = 1 - ssr / sst
print('R-square = %.4f' % R2)



#######예제
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

boston  = load_boston()
# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(boston['data'],boston['target'], test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)
print('train :{:.4f}'.format(model.score(x_train, y_train)))
print('test: {:.4f}'.format(model.score(x_test, y_test)))

###표준화 해서 하기
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Boston housing data set을 읽어온다
boston = load_boston()
#standardscaler
f_scale = StandardScaler()
t_scale = StandardScaler()
f_scaled = f_scale.fit_transform(boston.data)
t_scaled = t_scale.fit_transform(boston.target.reshape(-1,1))

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(f_scaled, t_scaled, test_size = 0.2)

# Logistic Regression으로 Train 데이터 세트를 학습한다.
model = LinearRegression()
model.fit(x_train, y_train)


# x_test[n]에 해당하는 target (price)을 추정한다.
n = 1
y_pred = model.predict(x_test[n].reshape(1, -1))

y_pred

# 복원
y_pred = t_scale.inverse_transform(y_pred)
y_true = t_scale.inverse_transform(y_test[n].reshape(-1, 1))

print('test[%d]의 추정 price = %.2f' % (n, y_pred))
print('test[%d]의 실제 price = %.2f' % (n, y_true))
print('추정 오류 = rmse(추정 price - 실제 price) = %.2f' % np.sqrt(np.square(y_pred - y_true)))

# 시험 데이터 전체의 오류를 MSE로 표시한다.
# MSE는 값의 범위가 크다는 단점이 있다.
y_pred = model.predict(x_test)
y_pred = t_scale.inverse_transform(y_pred)
y_true = t_scale.inverse_transform(y_test)

rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))
print('시험 데이터 전체 오류 (rmse) = %.4f' % rmse)

# 시험 데이터 전체의 오류를 R-square로 표시한다.
# 범위가 한정되어 MSE보다 좋은 척도다.
print('시험 데이터 전체 오류 (R2-score) = %.4f' % model.score(x_test, y_test))

y_pred

# 추정 결과를 시각화 한다.
plt.figure(figsize=(6, 6))
plt.scatter(y_true, y_pred, c='red', s=30, alpha=0.5)
plt.xlabel("house price")
plt.ylabel("predicted price")
plt.show()




#릿지, 라소, 엘레스티넷(릿지+라소)

from sklearn.linear_model import Lasso

lasso = Lasso()

lasso.fit(x_train, y_train)

lasso.score(x_train, y_train)























