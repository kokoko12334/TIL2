# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:57:24 2021

@author: User
"""

#iterator는 반복가능한 객체를 말함

dir([1,2,3])   #list클래스의 속성,메소드들을 보여줌

#보면 __iter__라고 있는데 이는 반복가능한 객체라는 의미
#iterable(반복가능한 객체)에서 .__iter__()를 붙힌것이 iterater(이터레이터)임. 이 두 개 구분해야함.



x=[1,2,3]
x.__iter__()  #이터레이터가 나옴 암튼 이상한저게 이터레이터임(이터레이터화)

it=x.__iter__()  #불러온 이터레이

it.__next__()  #계속실행하면  안의 값들이 순서대로 나오고 더이상 꺼낼게 없으면 stopiteration 이라고 나옴


a,b,c = it           #이터레이터는 다음과 같이 언팩킹 기능이 있음 단, 일회용 같음.
print(a,b,c)

a,b,c = map(int,input().split())    #이것도 이터레이터를 이용한 언팩킹 방식임.

#for의 동작과정
for i in range(1,4):
    print(i)

#range에서 이터레이터 __iter__로 뽑아내서 반복할 때마다
#__next__를 이용하여 i에 할당하고 이터가 없을 떄 까지 반복.




#39.2부(이터레이터 만들기)



class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self          #그냥 iterator를 정의한드는 뜻인 듯

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration



for i in Counter(5):
    print(i, end= '')


a,b,c = Counter(3)  ; a,b,c


a, _, c = Counter(3)  ;a,c   #두번째 자리는 비우겠다는 소리임.







#인덱스로 접근하는 이터레이터 만들기

class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):        #인덱스 칸인 []를 만들어준다고 생각
        if index < self.stop:
            return index
        else:
            raise IndexError

print(Counter(3)[2])








###내장함수 iter , next  앞에는 .__iter__()를 사용했다. 하지만 이번에는 iter()처럼 함수형임
#앞에서 배운 것
x = range(3).__iter__()
x.__next__()

#지금 배울 것
x= iter(range(3))
next(x)


#응용   iter(반복가능한 객체, 끝낼 숫자)
import random

x = iter(lambda: random.randint(0,5),2)     #0~4에서 2가 나오면 끝내겠다는 소리(이때 매개변수가 없는 lambda를 설정)
next(x)





x = iter(range(3))
next(x, 10)         #iter가 끝나면 10을 계속 출력함.






