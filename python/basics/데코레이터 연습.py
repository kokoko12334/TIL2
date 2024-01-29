
def add(a,b):
    return a+b

def sub(a,b):
    return a-b



def out():
    print('이야야야')


def wrapper(func):
    def pri(**kward):
        print(func.__name__, 'dddddd')
    return pri

def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling')
        return func(*args, **kwargs)
    return wrapper

add = logged(add)

add(1,2)





def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling')
        return func(*args, **kwargs)
    return wrapper
@logged
def sub(a,b):
    return a+b

sub(1,3)

del sub

add(1,2)



def ko(func):
    def wrapper(*args, **dic):
        print('안녕')
        print('das')
        return func(*args, **dic)
    return wrapper    
@ko
def add(a,b):
    return a+b
add(1,2)










