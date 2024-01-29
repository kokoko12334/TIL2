# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:30:14 2021

@author: user
"""



i=0
while i <100:
    print("Hello, world", i)
    i+=1                          #조건식에 만족(참)하면 코드내용을 계속실행, 아니면 중단함. 초기식을 무조건 주어야함.




count=int(input("반복할 횟수를 입력하시오"))

i=0
while i < count:
    print("hwll",i)
    i += 1


#랜덤함수 호출
import random

random.random()


random.randint(1,6)      #1~6까지 난수생성


#1~6사이의 난수를 생성하는데 3이 나오면 반복이 끝남

i=0         
while i != 3:
    i=random.randint(1,6)
    print(i)
    






while True:
    print("Hello, world!")           #조건이 참이면 코드를 실행하므로 다음 식은 무한루프가 됨. 콘솔창에서 컨트롤+C로 종료가능


a = [1,2,3,4]

while True:
    a.pop()          #마지막에 오류가 나옴

while a:
    a.pop()        #오류 없이 진행



##교통카드 차감
    
balance=int(input("처음잔액"))

while balance > 1350: 
    balance -=1350
    print(balance)
 




#기타 예시
prompt = """
1. 추가
2. 삭제
3.보기
4.그만
번호를 입력하세요:

"""
#num 4를 누르면 while문 종료
num = 0
while num != 4:
  num = int(input(prompt))
  print(f'{num}')





######


num_coffee = 10
price = 5000
money = int(input('돈:'))
if money >= price:
  
  while money:
    
    print('커피를 판매합니다')
    money -= price
    num_coffee -= 1  
    print(f'남은 커피는 {num_coffee}입니다')
    print(f'남은 잔액:{money}') 
    
    if money < price or num_coffee <= 0:
      
     print('커피 판매를 중지합니다.')
     break
  
elif money < price:
  print('잔액부족') 



######

















