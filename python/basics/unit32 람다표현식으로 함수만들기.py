# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:31:49 2021

@author: User
"""
#람다표현식으로 함수표현

def add(x):
    return x+10

#위 함수를 람다로 표현하기
#lambda 변수: 식
lambda x: x+10

#이를 쓰기위해서는 변수에 저장하면 됨

y = lambda x: x+10
y(1)

(lambda x: x+10)(1) #이와 같이 쓸수도 잇음
#단 람다식은 안에 변수를 넣을 수 없



a = [1,2,3,4,5,6,7,8,9,10]

list(map(lambda x: str(x) if x%3==0 else x,a))
#map(함수,데이터)   만약 3의 배수면 str(x)  else(아니면) 그냥 x 출력 그 출처는 a에서
#lambda식에서 if를 쓰면 반드시 else를 써야함 또한 elif를 쓸 수 없음.



a=[1,2,3,4,5]
b=[2,3,4,5,6]

list(map(lambda x, y: x*y,a,b))



#filter  True인 객체만 불러옴.
def f(x):
    return x>5 and x<10

a=[2,3,4,8,11,55]

list(filter(f,a))
#람다 표현식
list(filter(lambda x:x>5 and x<10, a))



#reduce(원소들을 순서대로 누적합)
from functools import reduce
reduce(lambda x,y: x+y,a)



