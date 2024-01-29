# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def printnumber(a,b,c):
    print(a)
    print(b)
    print(c)


x=[10,20,30]
printnumber(*x)  #언팩킹함.



#리스트안에 내용들을 각각 출력하는 함수 만들기



def pn(*x):
    for i in x:
        print(i)

y=[3,4,4,5,2,4,3,4,24,234,24,4]

pn(*y)
#딕셔너리자료는 **y로 해주어야함.

def dic(**kwarg):
    print(kwarg)



def infor(name, age, address):
    print('name is:', name)
    print('age is:', age)
    print('address is:', address)

infor('홍길동',30)   #변수가 3개인데 2개만 입력하는 오류가 나옴 이때 다음과 같이 초기값을 주면 됨.





def infor(name, age, address='비공개'):
    print('name is:', name)
    print('age is:', age)
    print('address is:', address)

infor('홍길동',30)

#이때 초기값은 맨 뒤에 있어야함 그래서 방법으로 다음과 같이 모든 변수에 초기값을 부여함.


def infor(name='비공개', age=0, address='비공개'):
    print('name is:', name)
    print('age is:', age)
    print('address is:', address)
infor()











