# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:29:40 2021

@author: User
"""
#반환값이라서 다른변수에 할당해주어야함.
s='hello, world!'
s.replace('world!', 'python!')

s1 =s.replace('world!', 'python!')
s1 



#문자변경 테이블
table = str.maketrans('abcde','12345')
'apple'.translate(table)



#문자분리
x='a b c'
y=x.split()
y
#문자합치기
' '.join(y)
'-'.join(y)

#대문자
c='python'.upper()
#소문자
c.lower()

#공백제거
'    python     '.lstrip()

'    python     '.rstrip()

'    python     '.strip()

',python,'.strip(',')


'python'.ljust(10) #10칸 사용하고 왼쪽부터 채우기

'python'.center(10)
#홀수면 왼쪽에 공백 한칸이 됨.

'python'.rjust(10).upper()




#왼쪽에 0채우기
'35'.zfill(10)


#문자열 인덱스 찾기
'apple pl'.find('pl')
'apple pl'.rfind('pl')  #오른쪽부터 훑음
'apple pl'.find('x') #없으면 -1로 반환

'apple pl'.index('pl') #이건 없으면 오류가 나옴
'apple pl'.rindex('pl')



#문자열 포메팅
'I am %s' % 'ko' #%s는 변수 %뒤에는 지정할 문자열

'i am %d years old' %10 #%d는 10진수

'%f'%3
'%.2f'%3 #소수점 두자리 표시
'%.3f'%3 #소수점 세자리 표시


'%10s'%'pyhthon'

'%-10s'%'pyhthon'


'Today is %d %s' % (3,'Aprill')

#더 간단한 포메팅
'hello {0}'.format(10)
'hello {0} {2} {1}'.format(10, 's', '20')

'hello {l} {v}'.format(l='222', v='12')

#더더 간단한 포메팅 앞에f를 붙
l=12
v=23
f'hello {l} {v}'




'{0:<10}'.format('ppppp')  #10칸의 자리를 만들고 '<'는 왼쪽부터 채워라

'{0:>10}'.format('ppppp')




'%03d' % 1   #03d는 세자리
'%04d' %35
'{:03d}'.format(1)

'{0:0>10.2f}'.format(15) #10개 칸 만들기 오른쪽부터 채우기, 소수점은 두자리까지

'{0:a>10.2f}'.format(15) #10개 칸 만들기 오른쪽부터 채우기 나머지는 a채우기, 소수점은 두자리까지


'%s %s'% ('h', 's')

