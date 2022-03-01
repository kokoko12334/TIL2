# @로 표현, 함수를 장식(무언가를 달다)한다는 뜻임. 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용함.


from re import X


def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')
 
def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')
 
hello()
world()

#함수를 추가할때마다 위처럼 항상 print를 추가해 주어야함.


# 데코레이터 만들기
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')   #.__name__은 func가 함수이므로 그 함수의 이름을 나타냄.
        func()                     #함수그대로 출력
        print(func.__name__, '함수 끝')
    return wrapper        #return 값을 받기 위해서 wrapper 함수를 쓴다.


def hello():
    print('hello')

def world():
    print('world')


trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출



### wrapper()를 안쓰는 경우
def trace2(func):
    print(func.__name__, '함수 시작')
    func()
    print(func.__name__, '함수 끝')


a = trace(hello)   #참고로 hello()괄호는 함수를 호출하는 것이고 hello 자체는 그냥 매개변수임
a()

b = trace2(hello)   
b()           #wapper가 없는 경우 return 값이 없어서 오류가 나온다.




##@ 사용하면서 데코레이터 하기

def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')   #.__name__은 func가 함수이므로 그 함수의 이름을 나타냄.
        func()                     #함수그대로 출력
        print(func.__name__, '함수 끝')
    return wrapper        #return 값을 받기 위해서 wrapper 함수를 쓴다.



@trace                      #위에서  a = trace(hello)   ,  a()  없이 진행하는 과정
def hello():                  #주의 할 것이 위에서 trace 함수도 같이 묶어서 해야함.
    print('hello')

@trace
def world():
    print('world')


hello()

world()
 

#매개변수와 반환값을 처리하는 데코레이터 만들기


def trace(func):
    def wrapper(a,b):
        r = func(a,b)
        print('{0}(a = {1}, b = {2}) ->{3}'.format(func.__name__, a,b,r))
        return r        #이거를 빼고 넣고 돌리면 차이를 알게 됨.
    return wrapper


@trace
def add(a,b):
    return a+b

add(10, 20)



##언팩킹(변수 갯수 지정하지 않음)

def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print( '{0}(args = {1}, kwargs = {2} -> {3}'.format(func.__name__, args, kwargs, r))
        return r
    return wrapper



@trace
def get_max(*args):
    return max(args)

@trace
def get_min(**kwargs):
    return min(kwargs.values())



print(get_max(10,20,30))

print(get_min(a = 10, b = 20))



#매개변수가 있는 데코레이터 만들기 (데코레이터 안에 매개변수가 있다는 뜻임.)



def is_multiple(x):
    def real_decorator(func):
        def wrapper(a,b):
            r = func(a,b)
            if r%x ==0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator    #그냥 내부함수를 반환 받고 그 반환값을 다시 반환한다고 생각

@is_multiple(3)
def add(a,b):
    return a+b

add(10,20)





#클래스로 데코레이터 만들기, 위에서는 함수를 데코레이터로 썻었음.
#이때는 함수를 매개변수로 받았을 때 이를 호출하는 __call__을 사용함.


class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 끝')


@Trace
def hello():
    print('hello')

hello()


# @Trace 데코레이터 없이 호출하려면은 다음과 같이 인스턴스화 한다음에 인스턴스()로 해당 함수를 호출함.
def hello():
    print('hello')

trace_hello = Trace(hello)

trace_hello()







#클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기


class Trace:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        print('{0}(args = {1}, kwargs = {2}) -> {3}'.format(self.func.__name__, args, kwargs, r))

        return r



@Trace
def add(a,b):
    return a+b

add(10,20)




#클래스로 매개변수가 있는 데코레이터 만들기


class IsMultiple:
    def __init__(self, x):
        self.x = x


    def __call__(self, func):
        def wrapper(a,b):
            r = func(a,b)
            if r%self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper


@IsMultiple(5)
def add(a, b):
    return a+b

print(add(10,20))




