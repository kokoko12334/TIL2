# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 00:11:40 2021

@author: user
"""

#1~101까지 출력 3의 배수를 Fizz 5의배수는 Buzz  3과 5의 공부새는 FizzBuzz출력하는 문제임


#step1

for i in range(1,101):
    print(i)



#step2
    
for i in range(1,101):
    if i%3==0:
        print('Fizz')
        
    elif i%5==0:
        print('Buzz')
        
    else:
        print(i)


#step3
        
for i in range(1, 101):                  #순서바뀌면 맨 위에거 부터 처리됨.
    if i % 3 == 0 and i % 5 == 0:    
        print('FizzBuzz')            
    elif i % 3 == 0:                 
        print('Fizz')               
    elif i % 5 == 0:                
        print('Buzz')                
    else:
        print(i)             


#다른 방법
        
for i in range(1, 101):      # 1부터 100까지 100번 반복
    if i % 15 == 0:          # 15의 배수(3과 5의 공배수)일 때
        print('FizzBuzz')    # FizzBuzz 출력
    elif i % 3 == 0:         # 3의 배수일 때
        print('Fizz')        # Fizz 출력
    elif i % 5 == 0:         # 5의 배수일 때
        print('Buzz')        # Buzz 출력
    else:
        print(i)             # 아무것도 해당되지 않을 때 숫자 출력















