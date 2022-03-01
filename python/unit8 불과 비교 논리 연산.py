# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:06:00 2021

@author: user
"""


10==5  #같다
10!=5   #같지 않다  문자열도 같은지 아닌지 비교가능



1 is 1.0         #객체형태를 비교함. 1은 int 이고 1.0은 float이므로 false가 나옴.

1 is not 1.0



True and True

True and False


True or False


not True

not False         

not True and False or not False   #not and or순으로 처리함.



bool(0)   #bool은 1은 T 0은 F로 판단하는 함수
bool(1)
bool("false")    #0이외의 값들은 다 T로 판단, 값이 있으면 무조건 T임.
bool('') 
bool(' ')   #빈공간도 먼가가 있다고 판단



k,e,m,s=map(float, input("국어, 영어, 수학, 과학순으로 쓰시오:").split(","))
print(k>=90 and e>80 and m>85 and s>=80)
 












