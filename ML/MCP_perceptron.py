import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron():
    #eta = 학습률, n_iter = 반복횟수, random_state = 가중치 랜덤 초기값
    def __init__(self, eta = 0.01, n_iter = 50, random_state = 1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
    
    def fit(self, x, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale = 0.01, size = 1 + x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(x,y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)

            self.errors_.append(errors)     
        return self

    def net_input(self, x):

        return np.dot(x, self.w_[1:]) + self.w_[0]

    def predict(self, x):

        return np.where(self.net_input(x) >= 0.0, 1, -1)  #값이 0보다 크면(True) 1, false면 -1




#붓꽃 데이터 불러오기
df = pd.read_csv('./data/iris_data.csv', header = 0)
df

y = df.iloc[0:100,4].values
y = np.where(y == 'setosa', -1, 1)

x = df.iloc[0:100, [0,2]].values

#산점도
plt.scatter(x[:50, 0], x[:50, 1], color = 'red', marker = 'o', label = 'setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color = 'blue', marker = 'x', label = 'versicolor')
plt.xlabel('sepal length')
plt.ylabel('petal lengh')
plt.legend(loc = 'upper left')
plt.show()


#모델 시행
ppn = Perceptron(eta = 0.1, n_iter = 10)
ppn.fit(x,y) #errors_ 랑 w_ 반환

#epoch에 따른 에러 갯수
plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker = 'o')
plt.xlabel('Epochs')
plt.ylabel('errors_count') 
plt.show()

















