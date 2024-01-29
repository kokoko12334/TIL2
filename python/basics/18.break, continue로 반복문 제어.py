# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:58:00 2021

@author: user
"""



i=0
while True:
    print(i)
    i+=1
    if i==100:
        break            #무한루프를 하다가 i=100이면 중단(break)    99까지 출력하고 1+99하고 i=100인지 물어봄=> 브레이크됨.



for i in range(10000):
    print(i)
    if i==100:
        break             #위와 차이점은 100을 출력하고i==100인가를 물어보므로 100까지 출력






for i in range(100):
    if i%2==0:
        continue
    print(i)                   #홀수만 출력하기, continue는 해당조건식이 참이면 다시 위로 올라가라(코드를 출력하지 말고) 그러다가 조건이
                                #맞지 않으면 그때 코드를 출력하라 따라서 홀수만 출력됨.



i=0
while i <100:
    i +=1
    if i%2 ==0:
        continue
    print(i)



#입력한 횟수만큼 반복하기
    

count=int(input("반복횟수"))

i=0
while True:
    print(i)
    i+=1
    if i==count:
        break




#홀수만 출력
count=int(input('반복횟수'))

for i in range(count+1):
    if i%2==0:
        continue
    print(i)





start, stop= map(int, input('start,stop').split(','))


i=start
while True:
     
     if i%10 == 3:
        i+=1             #3일때 continue로 3그대로 넘어가므로 +1을 해주어서 4로 넘어가게끔 해야함.
        continue
        
     if i==stop+1:
        break   
    
     print(i, end="   ")
     i += 1 
    
    
    
    


























