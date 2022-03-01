import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
import pandas as pd


#titanic
###########전처리
df = pd.read_csv('train.csv', sep=',')
df.head(3)
df.info()
df.isnull().sum()   # 결측치 개수 확인

df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', \
                                   'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Others')
df['Title'] = df['Title'].replace('Mlle', 'Miss')
df['Title'] = df['Title'].replace('Ms', 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')
df['Title'].value_counts()

df['Fare'] = df['Fare'] / (df['SibSp'] + df['Parch'] + 1)

# 결측치 처리. Cabin은 결측치가 너무 많아서 drop.
# df['Age'].fillna(df['Age'].mean(), inplace = True)  # 평균으로 대체 --> 나중에 regression을 추정해 볼 것.
df['Embarked'].fillna('N', inplace = True)
df.isnull().sum()   # 결측치 개수 확인

# 불필요한 feature를 제거한다.
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df.head()




# XGBoost를 이용해서 Age의 결측치를 추정해 보자

df = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title'])

df.head()
df.isnull().sum()
###age 훈련데이터

df_train=df.dropna(subset = ['Age'])
df_train.drop('Survived', axis =1, inplace = True)
#age를 종속변수 지정
age = df_train.pop('Age')
age
#df 에서 age가 결측치인 행만 뽑아오기(테스트)
age_test = df[df['Age'].isnull()]
age_test
age_test.pop('Age')
age_test.drop('Survived', axis =1, inplace = True)
##xgb모델
xgb_model = xgb.XGBRegressor(object = 'reg:squarerror')

xgb_model.fit(df_train, age)

age_pred=xgb_model.predict(age_test)
age_pred

##df에서 age가 결측치인 인덱스 번호 지정
age_n = df[df['Age'].isnull()].index

##예측값이랑 인덱스번호랑 dict로 묶음
age_r  = dict(zip(age_n, age_pred))

##fillna는 dict, pd.series로 예측값을 하나가 아닌 여러값으로 지정
df['Age'].fillna(age_r, inplace=True )
df.isnull().sum()

df.drop('Fare', axis = 1)









