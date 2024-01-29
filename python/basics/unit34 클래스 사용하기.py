
#클래스: 자료의 상태
#메소드: 그 자료의 상태(클래스)가 취 할수 있는 행동들
#속성: 그 클래스의 기본값() 괄호안에 집어 넣는 값
#인스턴스: 객체에 클래스를 부여
#class에 앞에는 무조건 대문자
#안의 메소드지정에서는 무조건 self가 와야함.

class Person:
    def greeting(self):       #메소드는 행동 즉 쓸 수 있는 것들을 다 표시함 이때 def로 정의
        print('hello')

s=Person()  #클래스를 지정하고(인스턴트화)

s.greeting()  #메소드를 쓰면됨.

##클래스를 이용한 계산
class Mul:
    def mul(self,a,b):
        return a+b

s = Mul()
c=s.mul(1,2)            #####그냥 def 정의해서 하는 거랑 같음.



#다른 예제
class Calc:

  def __init__(self, first=None, second=None):
    self.first = first
    self.second = second
  def add(self):
    return self.first+self.second
  def sub(self):
    return self.first-self.second
  def mul(self):
    return self.first*self.second
  def div(self):
    return self.first/self.second
    
ko = Calc(3,3)
ko.add()

#빈클래스
class Person:
    pass

#메소드 안에서 메서드 호출

class Person:
    def greeting(self):
        print('hello')
    def hello(self):
        self.greeting()   #hello()의 메소드를 다른 메소드를 이용해서 표현하려면 self.이 들어가야함.
        
    
s=Person()
s.hello()


#클래스 확인
isinstance(s,Person)

#다음과 같이 정수가 아니거나 음수일때의 조건에 쓰임.

def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)





#속성 사용하기

class Person:
    def __init__(self,name, age, address):      #속성의 변수를 정할 때는 self.변수명, 처음에는 self무조건
        self.hello='안녕하세요'
        self.name = name
        self.age = age
        self.address = address
        print('완료')  #init에 프린트를 넣으면 객체를 만들자마자(인스턴트화하자마자) 출력
        
    def greeting(self):
        print(f'"{self.name}, {self.age}입니다."')  #속성에 접근할 때는 self.변수
        #self.를 자꾸붙히는 이유는 그냥 그 클래스 안에서의 변수만들 사용한다고 생각




ko=Person('min',20,'jeju')
ko.greeting()
#속성을 호출할떄는 . 메소드 방식으로함

Person.__init__ #클래스의 속성 조회
dir(Person)  #클래스의 메소드 조회
ko.age
ko.name
ko.address
ko.hello



#클래스의 위치인수 (리스트)

class Person:
    
    def __init__(self, *args): #*는 언팩킹
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
        


maria = Person(*['마리아',20,'수원'])
maria2=Person('2',3,3)

maria2.age
#키워드 인수(딕셔너리)


class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1= Person(name = '마리아', age=20, address='ddada')
maria2 = Person(**{'name':'마리아','age':20,'address':'3333'})





#속성 추가

class Person:
    pass

maria=Person()
maria.name="koko"
maria.name

#단 해당 인스턴스에만 속성이 추가되고 다른 인스턴스(같은 클래스여도)는 추가가 안됨.




#다른 속성 생성 제한

class Person:
    __slots__ = ['name','age']


maria=Person()
maria.address="ddd"       #다른 속성 추가하려면 오류가 나옴.


#비공개 속성사용하기 self.__변수 형식으로 씀
class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age= age
        self.address = address
        self.__wallet = wallet  ##__를 붙힘.

maria=Person('마리아',20, '서울시', 10000)
maria.__wallet-=300 #클래스 바깥에서 접근하면 오류나옴

#비공개는 다음과같이 메소드로 접근해야함.

class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age= age
        self.address = address
        self.__wallet = wallet
    def pay(self, amount):
        self.__wallet -= amount
        
        print('이제 {0}원 남음'.format(self.__wallet))
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)


#쓰는 것보다 잔액이 적으면 다음과 같ㅇ이 출력


class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age= age
        self.address = address
        self.__wallet = wallet
    def pay(self, amount):
        if amount > self.__wallet:
            return '잔액 부족'
        self.__wallet-=amount
        print('현재 {0}원 납았음'.format(self.__wallet))
        
maria=Person(1,2,3,10000)

maria.pay(10000)

#간단하게 다음과 같이 메소드를 이용하여 비공개속성을 출력하도록 할 수 있음

class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age= age
        self.address = address
        self.__wallet = wallet
    def now(self):
        print(self.__wallet)
maria = Person('2',2,2,10000)
maria.now()

