# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:05:20 2021

@author: user
"""



for i in range(100):
    print("Hello, world")   #작동원리: range가 100개의 숫자가 있으므로 숫자가 있나?를 반복해서 코드 안의 것을 100번 반복함.




for i in range(100):
    print("Hello, world", end="",i)   #꺼내 쓰는 숫자를 확인



for i in range(4,15,2):
    print("Hello, world", i)   #꺼내 쓰는 숫자를 확인




for i in reversed(range(10)):
    print("Hello, world", i)




#반복하는 숫자 지정
    

count=int(input('반복할 횟수를 입력하시오'))

for i in range(count):
    print("h",i)



a=[10,20,30,40,50]

for i in a:
    print("hhh", a)          #요소가 5개 이므로 5번 반복. 



a=(10,20,30,40,50)

for i in a:
    print("hhh", a)          #요소가 5개 이므로 5번 반복. 




for letter in 'python':
    print("ㅁㅁ",letter, end="  ")      #문자열도 각 요소 대로 출력



##인수가 2개이상
num = [(1,2),(2,3),(3,4)]

for (a,b) in num:
    print(a-b)





result = [x*y for x in range(2,10) for y in range(1,10)]      #for문 안의 for문 실행임.x=2  -> y= 1~9까지 곱하고 그다음 x=3...9까지 진행
result
len(result)














