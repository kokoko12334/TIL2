from itertools import groupby
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

#KNN은 categorical 데이터에 사용하는데 제한이 있다.(거리를 가지고 계산하기때문에)

iris = load_iris()
#테스트 데이터
test = iris['data'][-1:] 
#타켓 데이터
y = iris['target']
#마지막 행을 제외한 데이터
data = iris['data'][:-1]
#거리구하기
distance=(((data-test)**2).sum(axis=1))**(1/2)

#거리 데이터와 타켓데이터 합치기
distance=distance.reshape((149,1))
y1 = y[:-1].reshape((149,1))
d_y = np.concatenate((distance, y1),axis=1)

#거리가 가장 작은 순서대로 정렬
d_y_sort=d_y[d_y[:,0].argsort()]


#거리가 가장 작은 데이터 10개
sample=d_y_sort[:11]
sample

#다수결
lst = [sample[i][1] for i in range(len(sample))]
element = set(lst)
cnt = [lst.count(i) for i in element ]
result = dict(zip(element,cnt))
print(max(result))


#KNN 함수
def knn(data, target, test, num = 10 ):
    distance=(((data-test)**2).sum(axis=1))**(1/2)

    distance=distance.reshape((distance.shape[0],1))
    target = target[:-1].reshape((target[:-1].shape[0],1))

    d_y = np.concatenate((distance, target),axis=1)
    d_y_sort=d_y[d_y[:,0].argsort()]
    sample=d_y_sort[:num+1]

    lst = [sample[i][1] for i in range(len(sample))]
    element = set(lst)
    cnt = [lst.count(i) for i in element]
    result = dict(zip(element,cnt)) 
    return max(result)

iris = load_iris()
#테스트 데이터
test = iris['data'][-1:] 
#타켓 데이터
target = iris['target']
#마지막 행을 제외한 데이터
data = iris['data'][:-1]

knn(data, target, test, 20)



##############################################
####강사
# iris 데이터를 읽어온다
iris = load_iris()

# 학습 데이터와 시험 데이터로 분리한다
x_train = iris['data'][:-1]
y_train = iris['target'][:-1]
x_test = iris['data'][-1:]

# 시험 데이터와 학습 데이터의 거리를 모두 계산한다.
distance = np.sqrt(((x_train - x_test) ** 2).sum(axis=1))

# 거리와 target을 dataframe으로 저장한다.
df = pd.DataFrame(data= np.c_[distance, y_train], columns= ['distance', 'target'])

# distance를 오름차순 (ascending)으로 정렬한다
df.sort_values(by='distance', inplace=True)

# distance가 큰 상위 K를 선택하고, target의 majority를 찾는다
K = 10
candidates = df[:K]['target'].to_numpy().astype('int')
counts = np.bincount(candidates)
majority = np.argmax(counts)
print(majority)

##########################################
#라이브러리
from sklearn.neighbors import KNeighborsClassifier
# KNN 모델을 생성한다.
knn = KNeighborsClassifier(n_neighbors = K)
knn.fit(x_train, y_train)  #인스턴트화

# 시험 데이터의 target을 추정한다.
y_pred = knn.predict(x_test)
print(y_pred)




#################################
###########가중치 KNN  ##############
###############################
iris = load_iris()

# 학습 데이터와 시험 데이터로 분리한다
x_train = iris['data'][:-1]
y_train = iris['target'][:-1]
x_test = iris['data'][-1:]

# 시험 데이터와 학습 데이터의 거리를 모두 계산한다.
distance = np.sqrt(((x_train - x_test) ** 2).sum(axis=1))

# 거리와 target을 dataframe으로 저장한다.
df = pd.DataFrame(data= np.c_[distance, y_train], columns= ['distance', 'target'])

# distance를 오름차순 (ascending)으로 정렬한다
df.sort_values(by='distance', inplace=True)

# distance가 큰 상위 K를 선택하고, target의 majority를 찾는다
K = 10
candidates = df[:K]['target'].to_numpy().astype('int')
candidates
counts = np.bincount(candidates)
counts
majority = np.argmax(counts)
print(majority)


######가중치##### 숫자가 높을수록 좋은거임
sample = df[:][0:10] ;sample

sample['weight'] = 1/sample['distance'] ;sample
##############
result = sample.groupby('target').sum()['weight'] ;result#갯수가 아니라 가중치의 합으로 나누어야함.

w_sum=sample['weight'].sum()

result=result/w_sum

result.idxmax()
#보면 groupby되고 target같이 인덱스넘버안에 있다 이거에 접근하려면 idx로해야한다.

################


#########강사########
# distance를 오름차순 (ascending)으로 정렬하고, 상위 K개를 선택한다
K = 10
df.sort_values(by='distance', inplace=True)
top_k = df[:K].copy()
top_k
# 거리 가중치를 계산한다. (inverse weighting)
top_k['weight'] = 1 / top_k['distance']
top_k
# 가중평균 거리를 계산한다.
w_distance = []
for t in [0, 1, 2]:
    w_distance.append(top_k.loc[top_k['target'] == t]['weight'].sum())
    print(top_k.loc[top_k['target'] == t]['weight'].sum())
w_distance /= top_k['weight'].sum()
w_distance
# w_distance가 가장 큰 class를 출력한다.
majority = np.argmax(w_distance)
print(majority)



###########라이브러리
from sklearn.neighbors import KNeighborsClassifier

# KNN 모델을 생성한다.
knn = KNeighborsClassifier(n_neighbors = 30, weights='distance')
knn.fit(x_train, y_train)

# 시험 데이터의 target을 추정한다.
y_pred = knn.predict(x_test)
print(y_pred)




####과제 적절한 k찾기
#train, test data 분류(8:2)

#test데이터의 거리를 다 각각 구하고
#그 값을 k개만큼 선택(작은것부터 )
#추정치의 정확도가 제일 높은 k찾기



###데이터 나누기
from sklearn.model_selection import train_test_split

iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size=0.2)

#테스트 데이터
accuracy_test = []
for k in range(1,101):
    knn = KNeighborsClassifier(n_neighbors = K, weights='distance')
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)

    cnt = 0
    for i in range(len(y_pred)):
        if y_pred[i]==y_test[i]:
            cnt += 1
        else:
            continue
    
    result = cnt/len(y_pred)
    accuracy_test.append(result)    
    print(f'k가 {k}일때 정확도 : {result}')

#트레인 데이터
accuracy_train = []
for k in range(1,101):
    knn = KNeighborsClassifier(n_neighbors = K, weights='distance')
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_train)

    cnt = 0
    for i in range(len(y_pred)):
        if y_pred[i]==y_train[i]:
            cnt += 1
        else:
            continue
    
    result = cnt/len(y_pred)
    accuracy_train.append(result)    
    print(f'k가 {k}일때 정확도 : {result}')    



import matplotlib.pyplot as plt
fig, ax= plt.subplots()
ax.set(ylim =(0,1.1))
ax.plot(accuracy_test, 'r--', label = 'test')
ax.plot(accuracy_train, 'b--', label = 'train')
ax.legend(loc = 'best')
plt.show()







#####knn.score 사용하기
knn = KNeighborsClassifier(n_neighbors = 20, weights='distance')
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size=0.2)

knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

knn.score(x_test, y_test)      #x_test를 모형에 집어넣고 그 결과를 y_test랑 비교한다.
acc_test =[]
acc_test.append(knn.score(x_test, y_test))

knn.score(x_train, y_train)
acc_train = []
acc_train.append(knn.score(x_train, y_train))


############knn(regression)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

x = np.array([1.25, 3.52, 3.0, 4.13, 6.51, 6.27, 7.3, 8.42, 8.81,
            10.14,10.68,12.6 , 13.42, 14.01, 14.82, 15.96, 17.77, 17.85]).reshape(-1,1)

y = np.array([ 5.64,  2.36, 11.08,  6.62,  9.18, 11.91,  5.61,  7.75, 12.16,
              18.18, 18.73, 20.43, 14.86, 26.75, 29.9 , 20.32, 25.04, 31.59])

x_test = np.array([ 1.98,  4.16,  3.43,  4.49,  6.51,  6.76,  7.31,  8.55,  9.69,
                    10.52, 10.85, 13.29, 13.63, 14.09, 15.28, 16.94, 18.01, 18.7 ]).reshape(-1,1)

plt.scatter(x, y, c='red', s=100)
plt.xticks(x, rotation=90)
plt.show()

# KNN regressor를 생성한다.(n_neihbors가 k임.)
knn = KNeighborsRegressor(n_neighbors=5, weights='uniform')
knn.fit(x, y)

# y를 추정한다.
y_hat = knn.predict(x_test)

# 추정된 y를 시각화하고, 육안으로 성능을 확인한다.
plt.scatter(x, y, c='red', s=100, alpha=0.7)
plt.plot(x, y_hat, marker='o', c='blue', alpha=0.7, 
         drawstyle="steps-post")
plt.show()

# x = 12.0일 때 y의 추정치는?
y_hat = knn.predict(np.array([12.0]).reshape(-1,1))
print("\nx = 12.0 --> predicted y = {:.4f}".format(y_hat[0]))

knn.score(x_test, y )



