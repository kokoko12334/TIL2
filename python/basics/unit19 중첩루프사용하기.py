# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 00:04:47 2021

@author: user
"""


for i in range(5):
 for j in range(5):
     print('j:', j, sep="", end="")
    
 print('i:', i, '\\n', sep='')





for i in range(5):            # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):        # 5번 반복. 안쪽 루프는 가로 방향
        print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()  






for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j <= i:                # 세로 방향 변수 i만큼
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)



















































