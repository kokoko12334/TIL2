# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:15:32 2021

@author: User
"""
#파일 작성
file= open('h.txt', 'w')
file.write('kokoko')
file.close()


#파일 불러서 읽기
file = open('h.txt', 'r')
s= file.read()
print(s)
file.close()


#file.close() 입력이 자동으로 닫아줌.
with open('h.txt', 'r') as file:
    s=file.read()
    print(s)


#여러줄 작성(반복)
with open('h.txt','w') as file:
    for i in range(3):
        file.write('heelllo {0}\n'.format(i))



#여러줄 작성
lines=['d\n', 'a\n']
with open('h.txt','w') as file:
    file.writelines(lines)


#읽기(문자열 그대로 리스트로 출력)
with open('h.txt', 'r') as file:
    lines=file.readlines()
    print(lines)


#예쁘게 출력
with open('h.txt', 'r') as file:
    line=None
    while line !="":
        line = file.readline()
        print(line.strip('\n'))

with open('h.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))




# 파이썬 객체를 파일에 저장
import pickle
name = "ko"
age=26
address= 'ddddddd'

scores={'e':100, 'm':99, 's':10}

with open('ko.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

#이렇게 하면 오류나옴 왜냐하면 .p로 저장해서(.txt는 사람이 알아보기 쉬움)
with open('ko.p', 'r') as file:
    s=file.read()
    print(s)
##############

#언피클링(열기)
import pickle

with open('ko.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)   
print(name)
print(age)
print(address)
print(scores)













##예제
f = open('매수종목.txt', 'w')

f.write('900260\n')
f.write('252670\n')
f.write('317240\n')

f.close()
##읽기
with open('매수종목.txt', 'r') as f:
  while True:
    line = f.readline()
    if not line:
      break
    print(line)  

#읽기(리스트로 만들기)
with open('매수종목.txt', 'r') as f:
   data=[]
   f=f.readlines()
for i in f:
  data.append(i.strip())
  
print(data)

#딕셔너리파일 넣기
stocks = {'로스웰':900260,'인버스':252670, 'TS':317240}

with open('매수종목1.txt', 'w') as s:
  for i,j in stocks.items():
    data = f'{i}:{j}\n'
    s.write(data)



#매수종목1 딕셔너리로 읽기
with open('매수종목1.txt', 'r') as s :
  s = s.readlines()
  print(s)   #확인용
  data = {}
  for i in s:
    k,v=i.strip().split(':')
    data[k]=v
  print(data)




import pickle

#binary 타입으로 쓰고 저장
with open('pickle_test.txt', 'wb') as f:     
    data = {1:'python', 2:'javascript'}
    pickle.dump(data, f)              



#불러오기(binary 읽기)

with open('pickle_test.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)

