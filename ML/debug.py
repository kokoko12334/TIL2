import pdb
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, KFold

iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)

cv = KFold(n_splits = 5, shuffle=True) 

depth_acc = []  # depth 별 정확도 리스트
for depth in range(1, 20):
    model = DecisionTreeClassifier(max_depth = depth)

    fold_acc = [] # k-fold 별 정확도 리스트
    for tx, vx in cv.split(x_train):  #train, eval 나누기
        # 학습용, 평가용 데이터
        xf_train, xf_eval = x_train[tx], x_train[vx]
        yf_train, yf_eval = y_train[tx], y_train[vx]
        ###중단점
        pdb.set_trace()
        # 학습
        model.fit(xf_train, yf_train)

        # 평가
        fold_acc.append(model.score(xf_eval, yf_eval))

    print("depth-{:2d} : fold acculate = {}".format(depth, np.round(fold_acc, 3)), end="")

    # fold 별 정확도 평균을 저장한다 = depth 별 정확도
    depth_acc.append(np.mean(fold_acc))
    print(" --> 평균 = {:.4f}".format(depth_acc[-1]))



#list면 진행상황
#print(변수)면 진행한데까지의 자료를 보여줌
#quit하면 나가짐.




