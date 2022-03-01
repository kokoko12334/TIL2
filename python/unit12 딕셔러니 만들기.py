# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:34:13 2021

@author: user
"""


lux={ 'health': 490, 'mana':334, 'melee':550, 'armor':18.72}

lux.values()  #밸류
lux.keys()      #키
lux.get('health')     #해당 키에 대응하는 밸류
lux.items() #키,밸류 다 출력
lux.clear() ;lux


#숫자에 대한 정보(위와 같이)와 묶을 때 나타냄.'{}'
#{키:값}이라고 함
#값에는 모든 자료형 가능 하지만 키에만 리스트[]  딕셔너리{}  불가능


x= {}   #빈공간
x

y=dict()   #딕셔너리 함수
y


#딕셔러니의 여러 표현방법 

#일반적인 방법
lux1=dict(health=490, mana=334, melee=550, armor=18.72)   
lux1

#zip방법
lux2=dict(zip(['health', 'mana', 'melee', 'armor'], [490,334,550,18.72]))  
lux2

#리스트 방법
lux3=dict([('health',490),('mana', 334),('melee', 550),('armor', 18.72)])  
lux3

#딕셔러니 방법
lux4=dict({ 'health': 490, 'mana':334, 'melee':550, 'armor':18.72})  
lux4



lux['health']  #키를 지정하면 그에 대응하는 값을 출력


lux['health']=2087  #값 변경
lux
lux['mana_regen']= 3.28    #없는 키를 없으면 해당 딕셔러니에 추가됨.
lux


'health' in lux
'health' not in lux


#2차원
price_dic = {'아메리카노': {'톨':1000, '그란데': 2000, '벤티':3000}, 
         '라떼': {'톨':100, '그란데':200, '벤티':300}}
price_dic['아메리카노']['톨']


price_list = {'아메리카노':[1000,2000,3000], '라떼':[100,200,300]}
price_list['아메리카노'][0]




a,b,c,d=input('체력, 체리, 마나, 마리').split(',')
a=int(a)
b=int(b)
c=int(c)
d=int(d)
print(dict(zip(['health','health_regen','mana','mana_regen'],[a,b,c,d])))




#기타

a = {(1,2):'b'} ;a  #튜플은 수정이 불가능 속성이여서 키로 사용가능

a = {[1,2]:'b'} ;a     #list는 오류나옴















































