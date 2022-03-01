# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:22:55 2021

@author: User
"""


#제너레이터는 yield 값을 이터레이터 요소로 인식하고 출력함.
def number_generator():
    yield 0
    yield 1
    yield 2

x = number_generator()

for i in x:
    print(i)
 


def number_generator():
    yield 0
    yield 1
    yield 2

x = number_generator()

next(x)
x.__next__()



##제너레이터 만들기

def number_generator(stop):
    n = 0
    while n < stop:
        yield n

        n += 1


g = number_generator(3)

next(g)
for i in g:
    print(i)



#######

def upper_generator(data):
    for i in data:
        yield i.upper()       #print랑 다른 점은 그냥 제너레이터를 생성한다는 것



x = ['a', 'b', 'c']
x_g=upper_generator(x)

for i in x_g:
    print(i)

############


##yield from으로 출력값 간단히 하기

def number_generator():
    x = [1,2,3]
    for i in x:
        yield i             #=> 요기 반복하는 부분을 yield from으로 간단히 할 수 있음.


for i in number_generator():
    print(i)


#변경 후

def number_generator():
    x = [1,2,3]
    yield from x         

for i in number_generator():
    print(i)


##참고


[i for i in range(50) if i%2==0 ]       #바로 요소들을 만들어냄


(i for i in range(50) if i%2==0)  # 소괄호()를 쓰면 제너레이터를 씀 이는 위보다 메모리 절약이 좋음.


