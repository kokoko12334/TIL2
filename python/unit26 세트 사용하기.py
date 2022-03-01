# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:29:16 2021

@author: User
"""

#세트는 집합을 말함 {}를 씀

f={'orange','apple','grape'}


'orange' in f
'orange' not in f

a=set('apple')
a
#중복을 제거 할때 쓰일 수 있음

a = [1,2,2,3,4]
a= set(a)
a


b=set(range(5))
b
c=set()
c
type(c)

#인덱싱
#집합은 순서가 없으므로 인덱싱을 할 수 없음. 따라서 리스트로 변경해서 진행함
a = {1,2,3,4}
a = list(a)
a[0]


#합집합
a={1,2,3,4}
b={3,4,5,6}
a|b 
set.union(a,b)

#교집합
a&b
set.intersection(a,b)



#차집합
a-b
set.difference(a, b)



#대칭 차집합
a^b
set.symmetric_difference(a, b)





#원소 추가/제거(연산후에 자동할당)

a |= {5}
a.update({10,11})  #여러개 추가
a.add(7)  #하나만 추가 가능
a


a &= {0,1,2,3,4,5}   #겹치는 것만 더함
a
a.intersection_update({0,1,2,3,4,5})
a


a -= {5}
a
a.difference_update({4})
a


a={1,2,3,4}
a ^={3,4,5,6}
a
a.symmetric_difference_update({3,4,5,6})
a




#부분집합
a={1,2,3,4}
a<={1,2,3,4,5}
a.issubset({1,2,3,4,5})

#진부분집합(같으면 안됨)
a<{1,2,3,4}
a<{1,2,3,4,5}



#상위집합
a={1,2,3,4}
a>={1,2,3}
a.issuperset({1,2,3})


#진상위집합

a>{1,2,3}
a>{1,2,3,4}



a=={1,2,3,4,}
a!={1,2,3}

#현재세트와 다른세트가 겹치는게 있는지 확인
#겹치는게 없으면 T 있으면 F
a={1,2,3,4}
a.isdisjoint({5,6,7,8})





#조작하기
a={1,2,3,4}
a.add(5)
a

a.remove(5)
a

a.discard(5)  #remove랑 같으나 없는 값이 되면 그냥 넘어감(오류가 없음)


a.pop()  #왼쪽 부터 제거


a.clear()  #다 제거



#for문을 이용한 출력

a={1,2,3,4}
for i in a:
    print(i)

#표현식
a={i for i in 'apple'}
a

a={i for i in 'apple' if i not in 'apl'}
a
















