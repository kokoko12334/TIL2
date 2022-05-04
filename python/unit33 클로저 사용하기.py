# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:31:50 2021

@author: User
"""

#지역변수 전역변수

x=10
def ko():
    global x
    x= 20
    print(x)

ko()
print(x)

#함수안의 x는 지역변수지면 global x를 쓰면 아예 글로벌 변수로 됨.


x=1
def A():
    x = 10
    def B():
        nonlocal x
        x= 20
        
    B()    #B()을 실행하라
    print(x)

A()  #지역변수
print(x) #글로벌

# 함수안의 함수는 알고리즘 순서:  x=10 -> B()실행, ->B가 머지-> def b()를 봄
#B는 x=20 이라고 함  이것을 실행 이때 원래 안쪽함수(B)의 지역변수는 상위계층의 함수에 영향을 주지않음
#반대로 상위 함수(A)는 그 안 쪽 함수에 영향을 미친다. 이때 nonlocal를 사용하면 그 안의 지역변수가 아니란 뜻
#으로, 이는 하위함수가 상위함수에 영향을 줄 수 있음. 만약 함수가 겹쳐있다면 가장 가까운 함수의 변수를 씀

#nonlocal vs global:    nonlocal은 로컬 안의 로컬의 관계이고  global은 로컬(어느 로컬이든 상관없음)대 글로버 관계이다.

#unit33.3클로저 사용하기 다시보기 이해못함



#클로저는 자역변수와 코드(함수)를 함께 묶고 싶을 때 사용함
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a*x+b
    return mul_add

c=calc()  #반드시 변수로 지정해주어야 함.
c(1)

def calc():
    a=3
    b=5
    return lambda x:a*x+b

c=calc()
c(1)

#지역변수 매번 수정


def calc():
    a = 3
    b = 5
    total=0
    def mul_add(x):
        nonlocal total
        total = total+a*x+b
        print(total)
    return mul_add

c=calc()
c(1)
c(2)
c(3)



###################
def add(a, b):
    return a + b
 
def substract(a, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    return a / b
 
func_lst = [add, substract, multiply, divide]
a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))
for func in func_lst:
    print(func.__name__, ":", func(a, b))












    