# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:43:48 2021

@author: user
"""




x=20
if x==10:
    print('10입니다.')
    
elif x==20:
    print('20입니다.')



x=21
if x==10:
    print('10입니다.')
    
elif x==20:
    print('20입니다.')

else:
    print('20도 10도 아님')



#자판기##
button = int(input('콜라:1, 사이다:2, 환타:3임'))

if button==1:
    print('콜라')
    
elif button==2:
    print('사이다')

elif button==3:
    print('환타')
    
else:
    print('없음')


#나이에 따른 교통카드 차감액#

age= int(input('나이를 입력하세요'))
balance=9000

if 7 <= age <= 12:
    balance -= 650
    
elif 13<=age<=18:
    balance -= 1050

else:
    balance -= 1250
print(balance)

























