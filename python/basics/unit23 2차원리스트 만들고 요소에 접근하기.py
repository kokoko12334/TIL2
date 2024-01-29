# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 19:23:52 2021

@author: User
"""
#안에 있는[]가 0행부터 시작, 그 안에 있는것은 열로 표현

a = [[1,2], [3,4], [5,6]]
a
a[0]
a[0][0]
a[2][1]=100000
a







# 반복문으로 2차원 리스트 요소 출력하기

for x, y in a:
    print(x,y)
    

#i의 처음 행인 [1,2]를 j에 보내고 j는 그 안의 것을 차례대로 리턴받아서 출력
for i in a:         
    for j in i:
        print(j, end=" ")
    print()      #줄바꿈 용도



for i in range(len(a)):  #행의 갯수
    for j in range(len(a[i])):  #열의 갯수
        print(a[i][j], end=" ")
    print()    



#while 문 사용하
i = 0
while i < len(a):
    x,y=a[i]         #a[0]=[1,2]이므로 x,y에 각각 할당가능
    print(x,y)
    
    i+=1



i=0
while i <len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j], end=" ")
        j+=1
    print()    
    i+=1


#리스트 할당하기
#1차원
a = []

for i in range(10):
    a.append(0)    
a

#2차원
a=[]

for i in range(3):
    line=[]
    for j in range(2):
        line.append(0)
    print(line)        
    a.append(line)    
a

#그외 기타 방법
a=[[0 for j in range(2)] for i in range(3)]
a


a = [[0]*2 for i in range(3)]
a


#열의 크기가 다른 2차원
a = [3,1,3,2,5]  #각 행마다의 열의 크기

b=[]

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)    

print(b)



#복사
a=[[10,20],[30,40]]
b=a.copy()
b[0][0]=500
a     #a도 같이 복사됨 이때는 deepcopy를 이용
import copy
a=[[10,20],[30,40]]
b=copy.deepcopy(a)
b[0][0]=500
a           #b만 변경됨.
b










 

    