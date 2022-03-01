# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 00:25:02 2021

@author: user
"""
import sys

def hello():
    print('Hello, world!')

hello()





def add(a,b):
    print(a+b)

x=add(10,20)           #print는 출력하고 변수지정이 안됨.



def add(a,b):
    return a+b

x=add(10,20)      #return으로 반환되어서 변수지정이 가능 안에 있는 값을 밖으로 꺼낸 다고 생각.

x







def add_sub(a,b):
    return a+b, a-b          #두개의 함수식을 한번에 처리

x,y=add_sub(20,10)

x
y


def our_max(x):
    a=sorted(x)[len(x)-1]
    return(a)




     
#486에 대응하는 비밀번호 만들기


def yonnha(x):
    y=str(x)
    a={4:"love", 8:"smile", 6:"kiss"}
    
    for i in y:
        print( a[int(i)], end="")


x=48668484



yonnha(x)



##여러변수를 넣기

def add2(*args):  #개수에 상관이 없음.
  result = 0
  for arg in args:
    result += arg
    print(result)
  return result

result= add2(1,2,3,4,5,6,7,8,9,10)    #1000번까지의 변수를 넣어도 오류가 안나옴.


##선택적인 함수 만들기
def cal(op, *args):
  if op == 'add':
     result = 0
     for i in args:
       result +=i
  elif op == 'mul':
     result = 1
     for i in args:
       result *= i
  else:
     return 0
  return result


result = cal('add', 1,2,3,4,5) ;result



def say_nick(nick):             #파라미터 확인
  if nick == '바보':
    return
  print('ddddddd')  