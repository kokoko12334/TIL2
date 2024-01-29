# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:54:38 2021

@author: User
"""

#회문판별이란 level과 같이 양옆이 같은것

w=input()

is_p = True
for i in range(len(w)//2):
    if w[i] != w[-1-i]:
        is_p=False
        break
print(is_p)


#기타 방법
#1
world='level'
list(world)==list(reversed(world))


#2
w = input()

print(w==w[::-1])

x='abced'
x[::-1] #배열을 뒤집음


#N그램

#2-그램
text="Hello"

for i in range(len(text)-1):
    print(text[i],text[i+1], sep='')



text='this is python script'
w=text.split(' ')
w

for i in range(len(w)-1):
    print(w[i], w[i+1], sep=" ")















