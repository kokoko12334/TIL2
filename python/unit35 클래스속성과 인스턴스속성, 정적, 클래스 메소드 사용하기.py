
class Person:
    bag= []

    def put_bag(self, item):
        self.bag.append(item)


james = Person()

james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
id(james.bag) ;id(maria.bag)  #같은 것을 공유함

#보면 class 속성은 모든 인스턴스가 공유하고 인스턴스 속성은 뒤에서 했던것처럼 def __init__로 정의해서 독립점임
#그리고 이때 클래스 속성은 self보다는 클래스명을 입력해서 클래스 속성을 부여한다는 의미를 확실시하는게 좋음

#클래스 속성
class Person:
    bag= []                     #클래스 속성

    def put_bag(self, item):
        Person.bag.append(item)

#인스턴스 속성
class Person:
    def __init__(self):           #인스턴스 속성, 즉 앞에 배웠던 것(__init__)은 정확하게는 인스턴스 속성을 말함.
        self.bag= []

    def put_bag(self, item):
        self.bag.append(item)


james = Person()

james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
id(james.bag) ;id(maria.bag)  #id가 다름

#보면 서로 다른 속성을 부여했음. 속성을 공유하는 것이 클래스 속성, 독립된 속성을 공유하면 인스턴스 속성




#비공개 클래스 속성

class Knight:
    __item_limit = 10
    
    
    def print_item_limit(self):
        print(Knight.__item_limit)

x=Knight()
x.print_item_limit()   #내부접근(메소드)
print(Knight.__item_limit)  #외부접근(오류나옴)




#정적 메소드: 인스턴스를 거치지 않고 바로 메소드를 사용

class Cal:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Cal.add(10,20)
Cal.mul(10,20)


#클래스 메소드(클래스 속성을 이용하여 메소드 만들기)

class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.



@classmethod
def create(cls):

    p = cls()
    return p





















