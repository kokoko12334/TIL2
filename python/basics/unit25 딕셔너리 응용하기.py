# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:09:29 2021

@author: User
"""
#키값 수정
x = {'a':1, 'b':2, 'c':3}
x.setdefault('e')
x
x.setdefault('f',100)
x


x.update(a=90)
x


#update은 키값이 문자열일때만 작동해서 키가 숫자이면 다음과 같이 해줌.
y= {1:'one', 2:'two'}

y.update({1:'ONE',2:'TWO'})
y

y.update([[1,'one'], [2,'two']])
y

y.update(zip([1,2],['ONE','TWO']))
y




#삭제
x = {'a':1, 'b':2, 'c':3}
x.pop('a')
x

x = {'a':1, 'b':2, 'c':3}
del x['a']
x

#맨 끝의 키값을 삭제하고 튜플로 반환함.
x = {'a':1, 'b':2, 'c':3}
g=x.popitem()


x = {'a':1, 'b':2, 'c':3}
x.clear()
x

#해당 키의 값 출력
x = {'a':1, 'b':2, 'c':3}

x['a']  #없는거 치면 오류남
x.get('a') #없는거 치면 None임
x.get('2222', 'nono')  #없는거 치면 'nono'를 반환함

#그 외의 메소드
x.items() #키값
x.keys()   #키
x.values()  #값


#리스트와 튜플로 딕셔러니 만들기
keys=['a','b','c','d']

x = dict.fromkeys(keys)
x


x = dict.fromkeys(keys,100)
x



#키 출력

x = {'a':1, 'b':2, 'c':3}

for i in x:
    print(i, end=" ")


#키값 출력

x = {'a':1, 'b':2, 'c':3}
for k, v in x.items():
    print(k,v)

#값 출력
x = {'a':1, 'b':2, 'c':3}
for v in x.values():
    print(v, end=" ")


#dictionary 표현식
keys=['a','b','c','d']

x = {key:value for key,value in dict.fromkeys(keys).items()}
x

#key
{key:0 for key in dict.fromkeys(keys).keys()}


#v키값 위치변환

{value: key for key, value in {'a':10, 'b':20, 'c':30}.items()}


#값을 기준으로 삭제하기 다시 새로운 생성 방법으로 적용
x = {'a':10, 'b':20, 'c':30, 'd':40}

x1={k:v for k,v in x.items() if v!=20}





#할당과 복사

x={'a':0, 'b':0, 'c':0, 'd':0}
y=x
#리스트처럼 한 객체를 가지고 공유하므로 수정값 공유이고 is true임.
x is y


y=x.copy()
x is y


x={'a':{'a1':3}}

y=x.copy()

y['a']['a1']=6
x             #문자열처럼 [][]두개면 카피해도 같이공유됨.

import copy
y=copy.deepcopy(x)
#deepcopy를 씀

