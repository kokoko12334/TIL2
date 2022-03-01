import numpy as np

#행렬화
lst = [[1,2,3],[4,5,6],[7,8,9]]
scoreNdarray = np.array(lst)

x = np.array([[3,2],[1,4],[2,10]], dtype = np.int8) ;x  #int8비트
x


#정렬
x = np.array([[3,7],[1,4],[2,10]], dtype = np.int8) ;x  #int8비트
x
#####모든 행,렬이 따로 따로 정렬이됨.
x.sort() ;x
np.sort(x, axis=1)  #기본값은 행 정렬
np.sort(x, axis=0)


#원하는 행,렬 기준으로 정렬(같이 움직임)   
x.argsort() #행기준으로된 정렬을 인덱스로 반환
x = np.array([[3,7],[1,4],[2,10]], dtype = np.int8) ;x
r=x[:,0].argsort(axis=0) #0열기준으로 정렬 이것을 다음과 같이 인덱싱해주면됨.
x[r]



d_y_sort=d_y[d_y[:,0].argsort()]
#연산

scoreNdarray+1

scoreNdarray*2


#함수
#axis=0 은 열기준  axis=1은 행기준
scoreNdarray
np.sum(scoreNdarray)
np.sum(scoreNdarray, axis =0)    
np.sum(scoreNdarray, axis =1)    

np.mean(scoreNdarray)
np.mean(scoreNdarray, axis =1)



sample2D = np.random.rand(2,2) ;sample2D  #0~1사이의 난수

sample2DList = sample2D.tolist() ;sample2DList  #리스트화



y = x.T ;y  #전치행렬
x.strides #(행간 이동할때, 열간 이동할 때)
y.strides


np.average(range(1,11), weights=range(11,1, -1)) #가중치 weights에 값을 각각 할당함.



sample2D.dtype #객체 안의 요소 확인


floatArray = np.array([[1.,2],[3,4]])  #하나라도 .을 찍어주면 다 실수임.



a = np.array([[1,2,3],[4,5,6],[7,8,9]])

np.empty((4,3))  #완전 0근처의 값을 생성함.
np.empty_like(a) #a행렬의 차원만큼 쓰레기값생성




np.zeros((2,3))  #0행렬
np.zeros_like(a)


np.ones((2,3))   #1로 채워진 행렬
np.ones_like(a)



np.identity((3))  #단위행렬
np.eye(3,4)  #단위행렬중에서 정방행렬이 아니어도 됨.
np.eye(3,5,3) #1이 시작하는 열을 나타냄 0을 기준으로 시작함.



np.full((2,3),10)


np.arange(10) #range()랑 같음.
a = np.arange(4).reshape(2,2) ; a #range에서 행렬기능 추가     


np.linspace(2.0, 3.0,num=5)  #2부터 3까지 5개의 요소를 생성




a
np.amin(a, axis=0) #열기준최소값
np.amax(a, axis=0)

b = np.arange(9).reshape(3,3); b
np.ptp(b, axis = 0) #열기준으로 최대값-최소값

np.median(b, axis=0)  #중위값
np.var(b, axis=0) #열기준으로 분산
np.std(b, axis=0) #열기준 표편







#인덱싱

a = np.arange(12).reshape(3,4) ;a

a[0:2,0:3]  #r프로그램이랑 다른점은 마지막 인 a:b에서 b는 -1이고 0부터 시작이라는 점.
a[:2,:]
a[:2,]
a[0][0]
a[0,0]
a[[0,2],]

a.shape #행렬
a.ndim #차원


###중요 인덱신/슬라이싱 차이점

c = a[:,0:1] ;c #슬라이싱 방법임  (괄호가 다 다름)
c.shape
c.ndim #괄호갯수 파악



d = a[:,0] ;d #인덱싱방법(괄호안에 다 포함) 인덱싱을 하면 차원이 낮아짐
d.shape #1차원이니까 이 3은 요소의 갯수
d.ndim






###하나만 뽑앗을때, 행렬을 뽑았을 때의 차이
a = np.arange(12).reshape(3,4) ;a

b = a[0:1, 0:1] ;b   #복사함.
b= 1 ;a



c = a[1:3, 1:3]   #그 부분을 떼어다가 원본을 그대로 씀 따라서 변경내용이 a에도 반영됨.
c[0,0] = 100 ;a




#불리언
a = np.arange(1,7).reshape(3,2) ;a

bool_idx = a>2 ;bool_idx
a[bool_idx]  #True만 출력


#행렬 변환
a = np.arange(6)

a.reshape((2,3))
np.reshape(a, (2,3))
a = np.arange(6).reshape((2,3)) ;a
a = np.arange(6).reshape(-1,3) ;a  #-1의 뜻은 행은 냅두고 열에 따라 가변적으로 바뀜을 의미
a = np.arange(6).reshape(3,-1) ;a  #-1의 뜻은 열은 냅두고 행에 따라 가변적으로 바뀜을 의미

#1차원 배열로 만들기
a = np.arange(6).reshape((2,3))

np.reshape(a, 6)   #요소의 갯수를 쓰면 1차원으로 변경

a.ravel() #원본을 씀., 변경내역이 연결됨
np.ravel(a)

a.flatten()  #복사본으로 변경내역이 연결이 안됨.



#행렬 합치기
a = np.array([[1,2]])

b= np.array([[5,6]])

np.concatenate((a,b), axis = 0) #열기준으로 합침

np.concatenate((a,b.T), axis = 1)  #행기준으로 합침.  이때 b는 2행1열로 바꾸어야 함.

a.shape
b.T.shape



#내적
x = np.array([1,2])
y = np.array([5,6])


x.dot(y)  #내적 2*2행렬임
np.dot(x,y)


#브로드캐스트
v = np.array([1,0,1]) ;v
x = np.array(range(1,13)).reshape((4,3)) ;x

v+x  #자동으로 맞추는 기능이 브로드캐스팅임. 


#그 외 (행의갯수, 반복횟수)
vv = np.tile(v, (4,1))  #v를 4행 성성
vv

vvv = np.tile(v, (4,2))
vvv






