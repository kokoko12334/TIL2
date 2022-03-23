from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Dense  #레이어, 입력층, 은닉층
from tensorflow.keras.models import Model       #모델 생성
from sklearn.datasets import load_breast_cancer

canser = load_breast_cancer()
x_feat = canser['data']
y_target = canser['target'].reshape(-1,1)
x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, target_size=0.2)



#factor 갯수 만큼 입력층을 배치 Non은 all, 데이터가 들어오는 데로라는 뜻.
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층 Dense(은닉층 갯수)(연결할 입력층)
hLayer = Dense(10)(xInput)

#출력층 출력이 될 동그라미(1개)  sigmoid는 binary classification 
#마지막은 은닉층과 출력층 연결
yOutput = Dense(y_train.shape[1], activation = 'sigmoid')(hLayer)


#모델
model = Model(xInput, yOutput)

#학습 방법을 설정한다.
model.compile(loss = 'binary_crossentropy', optimizer = 'adam') 
#이진분류는 'binary-crossentropy'
#optimizer은 최소점을 찾는 방법

#학습을 시킴
model.fit(x_train, y_train, epochs = 100)


#평가
y_prob = model.predict(x_test) #0~1의 값을 가짐(sigmoid)

y_pred = (y_prob >0.5).astype('int8')  #1의 기준


acc = (y_test == y_pred).sum()/y_test.shape[0]
acc = (y_test == y_pred).mean()  #좀더 편리하게











