# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:02:03 2021

@author: user
"""


x=10
if x==10:
   print('10입니다')


if x==10:
    pass     #나중에 처리할 때 지금말고



x=15
if x >= 10:
    print('10이상')
    
    if x == 15:
        print('15입니다')
        
    if x == 20:
          print('20입니다')        #if 중첩처리하는 방법 이때 x>=10 아래 들여쓰기된 if는 ifx>=10을 만족해야 진행하는 식임.
          






x=int(input('숫자임력:'))

if x==10:
    print('10임')
    
    
if x==20:
    print('20임')




price=int(input('가격'))       #인풋을 다른줄로해서 묶을 수도 있음.
c=input('쿠폰')

if c=='cash3000':
    price -= 3000
    
if c=='cash5000':
    price -= 5000
    
print(price)


















