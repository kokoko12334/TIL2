# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:20:13 2021

@author: user
"""


y="Hello world"
y
type(y)

x,y,z=10,20,30
x,y,z
print(x,y,z)


x=y=z=10
print(x) ;print(y) ;print(z)


del x #x변수를 삭제


x=None   #텅 비어있는 상자 같은 것은 만듬 (null)
x
print(x) 



a = 10
a = a + 20
a                #변화를 계속 유지

a=10
a +=20
a                #위식을 변수 두번 입력을 방지하는 방법



input()    #콘솔창으로 처리해야함-->>>>>> #나는 ctrl+2하면 콘솔창으로 넘어감. 다시 돌아올때는 ctrl+3

x=input()
x


x=input('문자열을 입력하세요: ') #프롬프트라고도 하며 용도를 알려줌.


a=input('첫번 째숫자를 입력하세요:')
b=input('두번 째 숫자를 입력하세요:')
print(a+b)                             #input은 항상 문자열로 처리하기 때문에 a+b는 1020임.



a,b=input('문자열 두개를 입력하세요:').split()  #공백을 기준으로 분리
print(a)
print(b)



a,b=input('문자열 두개를 입력하세요:').split()  #input은 문자열 처리니까 int를 
a= int(a)
b= int(b)
print(a+b)



a,b=map(int, input('숫자 두개를 입력하세요: ').split(','))   #split에 분리하고자 하는 기호를 넣음.
print(a+b)



a,b,c=map(float, input('숫자 세개를 입력하세요:').split(','))
print(a+b+c)


a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
 
print(a + b)

#다음과 같이 변수를 list로 묶어서 하면 n개의 변수를 받을 수 있다.
A = list(map(int, input().split()))

##출력방법###
 

print(1,2, sep=" , ")
print(1,2,sep="")
print(1,2)             #위랑 차이점은 위는 붙혀서, 이것은 떨어져서 출력


print(1,2,3, sep='\n')   #줄바꿈되서 출력됨.



print(1,2,3, sep='\t')   #띄어서 출력함.
print(1,2,3, sep='\\')   #\표시를 하고 싶으면 \\두번을 쓴다.


print(1, end='')
print(2, end='')
print(3)                       #prtin 3개를 써서 한줄에 나열하는 방법 쓸모는 없어보임.


year, month, day, hour, minute, second = input("연도, 월,일,시간,분,초를 입력하세요:").split(",")

print(year, month, day, sep="-", end='T')
print(hour, minute, second, sep=":")




##기타
#슬라이싱에서
a=[1,2,3,4]

a[::-1]   #reverse()랑 같음. 혹은 sort(reverse=True)






































