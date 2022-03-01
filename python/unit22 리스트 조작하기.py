# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#append
a= [10,20,30]
a.append(500)
a

a=[]
a.append(10)
a

#extend (list list 추가)
b=[1,2,3]
a.extend(b)


#insert
a.insert(1, 399)


#pop 아무것도 없으면 마지막 것만 삭제
a.pop()
a.pop(0)
a

del a[0]


#remove는 특정값(인덱스가 아님)
a.remove(30)
a




a=[10,20,30,20,40,50]


a.index(20)
#중복된 값은 맨 앞의 인덱스값을 출력

#특정값의 갯수 확인
a.count(20)

#배열을 반대로 바꿈.
a.reverse()
a

#정렬 default값을 오름차순
a=[5,3,4,9,1,3]
a.sort()   #오름차순

a.sort(reverse=True)  #내림

sorted(a)  #이건 반환값
a

#clear  요소를 다 지움

a.clear()

del a[:]  #del을 이용한 삭제




#append없이 추가하기

a=[10,20,30]

a[len(a):]=[500]

a


#리스트 복사
b=a    #리스트 하나임 하나라도 수정하면 같이 수정됨

b=a.copy() #리스트 두개

a is b  #F
a == b  #T



#반복문으로 리스트 요소 출력

a=[34,54,64,14]

for i in a:
    print(i)



enumerate(a)
#요소, 인덱스 동시에 출력

for index, value in enumerate(a):   #eumerate은 변수와 인덱스를 튜플형식으로 반환
    print(index, value)
#index, value는 임의의 변수


#start=1은 index의 표시를 1부터 표사
for i, v in enumerate(a, start=1):
    print(i,v)



#while로 반복문 출력
i=0
while i <len(a):
    print(a[i])
    i+=1




#리스트의 가장 작은 수 큰수 구하기
a=[38,21,53,62,19]
s=a[0]
for i in a:
    if s>i:
        s=i
print(s)


a.sort()
a[0]
min(a)
#제일 큰수
a=[38,21,53,62,19]
s=a[0]
for i in a:
    if s<i:
        s=i
print(s)

a.sort(reverse=True)
a[0]


#반복문을 이용해서 합구하기
x=0
for i in a:
    x+=i
print(x)

sum(a)


#리스트 표현식(반복문 이용)

a=[i for i in range(10)]
a
b=list(i for i in range(10))
b


#i에 연산도 가능

c=list(i*2 for i in range(10))
c



#짝수만 지정
a = list(i for i in range(10) if i%2==0)
a




#변수를 여러번 지정 가능 (구구단 생성)

a = list(j*i for i in range(2,10) 
             for j in range(1,10))
a



#map활용

a=[1.1,2.2,3.3,4.5]
a=map(int,a)
for i in range(len(a)):
    a[i]=int(a[i])

# 이렇게 매번 어떤 함수를 써서 바꾸려면 번거로움
#list로 만들므로 앞에 list, tuple이면 튜플로 씀
a=list(map(int, a))
a


a=list(map(str,range(10)))
a




# 2의 거듭제곱만 나오기


a,b=map(int, input().split())
 

x=list(2**i for i in range(a,b+1))

x












