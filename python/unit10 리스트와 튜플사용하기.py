# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 00:36:47 2021

@author: user
"""


a=[1,2,3,4,5]
a




person=['james', 17, 12.3, True]

type(person)


###빈 리스트 만들기
a=[]
a

b=list()
b

##range
range(10)


a=list(range(10))  #9까지 생성

b=list(range(5,12))  

c=list(range(1,10,2))
c


d=list(range(10,0,-3))
d



###튜플 ()


a=(1,2,3,4,5)          #튜플의 특징은 저장된 요소를 수정,삭제가 불가능함.
a

k=38,            #튜플 형태를 유지하기 위해서 씀
type(k)

a=tuple(range(0,10))
a

#리스트를 튜플,  튜플을 리스트로 변경 가능
a=[1,2,3]

a1=tuple(a)
a1


a=input('입력하시오:')  
a=int(a)
print(tuple(range(-10,10,a)))

#vs코드에서는 ctrl+f5눌러야 함.


#####패킹 언패킹###
cell = 1,2,3,4,5  #packing
a,b,c,d,e =cell  #unpacking
print(a,b,c,d,e)      #해당 값에 대응되는 요소가 출력됨.


a = [1,2,3,4,5]      #list도 됨.
[e,f,g,h,i] = a






