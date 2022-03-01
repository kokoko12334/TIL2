# Regression tree 연습
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

boston = load_boston()

df = pd.DataFrame(boston['data'], columns= boston.feature_names)
df['PRICE'] = boston['target']
df.head()


x_train, x_test, y_train, y_test = train_test_split(boston['data'],boston['target'], test_size=0.2, random_state=30)

depth = range(1,100)
result = []
for d in depth:
    
    reg = DecisionTreeRegressor(max_depth=d)
    reg.fit(x_train, y_train)
    s = reg.score(x_test, y_test)
    result.append(s)
    print(f'depth: {d}, score:{s}')
print(f'max_score: {max(result)}, depth:{np.argmax(result)+1}')    

plt.plot(depth,result , 'o--')
plt.xlim = (1,21)
plt.ylim = (0,1.1)
plt.xlabel('depth')
plt.ylabel('score')
plt.show()



################FM 과정###train eval, test

#for d in depth:
#    reg = DecisionTreeRegressor(max_depth=d)
#    reg.fit(x_train, y_train)
#    s = reg.score(x_eval, y_eval)

# score가 가장 큰 depth를 넣음 이때 k라고 한다면(최대 depth가)

#reg = DecisionTreeRegressor(max_depth=k)

#reg.fit(x_train, y_train)

# reg.score(x_test, y_test) => 최종평가