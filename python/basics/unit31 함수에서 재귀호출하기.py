# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:47:13 2021

@author: User
"""

#재귀호출이란 다음과 같이 함수안에 자기 함수를 두는 것(무한루프처럼)
def hello():
    print('hello, world!')
    hello()

hello()



#다음과 같이 내가 원하는 수만큼 반복가능

def hello(count):
    if count == 0:
        return        #count=0이면 반환하고 재귀호출을 끝낸다.
    print('hello, world!', count)
    count -= 1
    hello(count)

hello(10)



#factorial 구하기

def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)





#피보나치 수열

n=int(input())

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)

print(fib(n))












