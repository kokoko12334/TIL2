#클래스 상속이란 기반클래스(위뿌리)에서 파생클래스(아래)로 속성이나 메소드가 전달됨을 의미(코딩의 중복 방지)
#메소드는 그냥 쓸수 있고 속성은 super을 써주어야 함.

#사람-학생 클래스 만들기

class Person:
    def greeting(self):
        print('hi')

    
class Student(Person):           #이름(class) 를 넣으면 해당 클래스로 상속이 됨.
    def study(self):
        print('go')


ko = Student()
ko.greeting()
ko.study()



#다른 예제
class Calc:

  def __init__(self, first, second):
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

class SafeCalc(Calc):
  def div(self):
    if self.second ==0:
      return
    else:
      return self.first/self.second  

c = SafeCalc(4,1)
c.div()        #이때 div()에서 0으로 나누면 나오는 오류를 반환값으로 처리(Nontype)

class Safecalc(Calc):
    def div(self):
        if self.second != 0:
            return self.first/self.second

class SafeCalc(Calc):          
  def div(self):
    if self.second !=0:
      return self.first/self.second 

c = SafeCalc(4,0)
c.div()    #0이므로 아무것도 안나옴(오버라이딩은 파생클래스 우선)이고 
           #if에서 조건에 맞지않는 것이 있다면 무조건 nontype 자동 반환







#####포함관계
#포함관계란 해당 클래스의 인스턴스(속성,메서드?)를 사용할 때 포함관계라고 함

class Person:
    def greeting(self):
        print('hi')


class Person_list:
    def __init__(self):
        self.person_list=[]

    def append_person(self, person):
        self.person_list.append(person)







###기반클래스 속성 사용하기


class Person:
    def __init__(self):
        print('person')        #이건 그냥 person, student 클래스를 구분하기 위해 사용
        self.hello= '안녕'


class Student(Person):
    def __init__(self):
        print('student')
        self.school='ddd'


x = Student()

x.school    #student 속성에는 정상적으로 나옴
x.hello    #하지만 기반클래스인 person의 속성은 오류가 나옴 이는 person의 init이 호출이 안되서 그럼



##해결 방법=> super()로 기반 클래스의 init를 호출함.

class Person:
    def __init__(self):
        print('person')       
        self.hello= '안녕'


class Student(Person):
    def __init__(self):
        super().__init__()        #기반클래스의 init호출  이때 init에 다른 변수가 있으면 그것도 설정해주어야함.
        print('student')
        self.school='ddd'

x = Student()
x.hello      #호출됨.


#만약에 하위클래스에 init이 없다면 다음처럼 하면됨. 이때 pass 밑에 메소드를 정의 해도됨.


class Person:
    def __init__(self):
        print('person')       
        self.hello= '안녕'

class Student(Person):
    pass

x = Student()
x.hello


#다른 예제

class Car:       #super     이때 init에 다른 변수가 있으면 그것도 설정해주어야함.
  def __init__(self, wheel,engine):
    self.wheel = wheel
    self.engine = engine

class Truck(Car):
  def __init__(self, wheel,engine, luggage):        #기반 클래스의 속성을 여기서도 언급을 해주어야 함.
    self.luggage = luggage
    super().__init__(wheel, engine)







####메소드 오버라이딩


class Person:
    def hello(self):
        print('안녕(기반)')

class Student(Person):
    def hello(self):
        print('안녕(파생)파이선 입니다.')

x = Student()

x.hello()

#오버라이딩은 기반 클래스와 파생 클래스의 메소드 네임이 일치하면 기반 클래스를 무시하고 파생 클래스를 호출함.
#이때 기반클래도 호출하고 싶으면 super()를 씀. 이는 다음과 같이 '안녕'의 중복을 방지하는데 쓰임.

class Person:
    def hello(self):
        print('안녕(기반)')

class Student(Person):
    def hello(self):
        super().hello()
        print('파이선 입니다.')

x = Student()

x.hello()





######################다중 상속


class Person:
    def person(self):
        print('안녕 사람입니다')

class University:
    def university(self):
        print('안녕 경기대학교에 다니고 있습니다.')

class Student(Person, University):
    def hello(self):
        print('안녕 학생입니다.')


x= Student()
print(x.hello(), x.person(), x.university())

#####다이아 몬드 상속
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
 
x = D()
x.greeting()    # 안녕하세요. B입니다.라고 나옴 이는 왼쪽(B)부터 읽어드림.

#클래스 상속되었을 때 출력되는 순서를 나타냄 첫번째로 D, 그다음은 B.... 쭈욱 순서대로임., 클래스이름으로 접근해야함.
D.mro()




#######추상클래스
#추상 클래스는 상속받은 파생 클래스의 메소드목록들을 강제하기 위해서 사용함
from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractclassmethod
    def study(self):
        pass
    @abstractclassmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('go study')

 
x = Student()   #애초에 할당이 안됨  이유는  추상클래스인 go to school를 정의하지 않아서임

x.study()       




class StudentBase(metaclass=ABCMeta):
    @abstractclassmethod
    def study(self):
        pass
    @abstractclassmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('go study')

    def go_to_school(self):
        print('gogogo')
 
x = Student()
x.study()
x.go_to_school()














def f(x):
    if x == 0:
        print('ko')











