# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:26:46 2021

@author: User
"""




try:
    x=int(input("숫자를 입력하시오:"))
    y=10/x
    print(x)
    
except:  #예외가 발생하면 다음을 실행하시오.
    print('예외가 발생하였씁니다.')    






y = [10,20,30]

try:
    index, x= map(int,input('인덱스와나룰 숫자입력').split())
    print(y[index]/x)
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')

except IndexError:
    print('잘못된 인덱스 입니다.')





#에러 코드와 함께 출력하기
y = [10,20,30]

try:
    index, x= map(int,input('인덱스와나룰 숫자입력').split())
    print(y[index]/x)
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.', e)

except IndexError as e:
    print('잘못된 인덱스 입니다.', e)


##모든 예외는 Exception을 사용하면 됨. 단 처음에 발생한 에러만 출력함.
try:
    
    a = [1,2,3]
    print(a[4])
    4/0
except Exception as e:
    print(e)


#else finally

try: 
    x=int(input('나룰 숫자를 입력하세요:'))
    y=10/x
except ZeroDivisionError: #예외이면 실행
    print('0으로 나눌 수 없음')    
else:       #예외가 아니면 실행(그냥 try안에 넣는 것이 편함)
    print(y)
finally:     #항상실행 (굳이 안써도 됨)
    print('코드 실행이 끝났씁니다.')



#예외발생시키기


try:
    x=int(input('3의배수를 입력하시오:'))
    if x%3 !=0:
        raise Exception('3의 배수가 아니다')
    print(x)    

except Exception as e:
    print('예외발생',e)

#함수를 정의하고 그 안에 넣어도 됨.
def three():

    x=int(input('3의배수를 입력하시오:'))
    if x%3 !=0:
        raise Exception('3의 배수가 아니다')
    print(x)    


try:
    three()
    
except Exception as e:
    print('예외발생',e)



#예외 만들기

class Nooo(Exception):     #상속받기
    def __init__(self):
        super().__init__('3의배수가 아니다')


class Nooo(Exception):     #이것도 가능 둘중 하나 써도 됨.
    def __str__(self):
        return '3의배수가 아니다'



def three():
    try:
        x=int(input('3의 배수를 입력하시오:'))
        if x%3 !=0:
            raise Nooo
        print(x)    
    except Exception as e:
        print('예외발생',e)

three()
##다른 예제
class Bird:
    def fly(self):
        raise NotImplementedError
        

class Eagles(Bird):
    pass


eagle = Eagles()

eagle.fly()





#while 문과 예외처리를 이용하여 remove의 내용 다 지우기.
   
a=[1,2,3,1,2,3,1,2,3]
while True:
    try:
        a.remove(3)
        
    except Exception as e:
        print(e)
        print(a)
        break






###기타




try:
  nums = ['10.22', '', '8.00']

  for num in nums:
    print(float(num))

except Exception as e:
  print(0)
  print(e)




##for 안에 try를 넣는 것이 좋음.
lst = []

for num in nums:
  try:
    lst.append(float(num))
  except Exception as e:
    lst.append(0)
print(lst)

data  = [1, 2, 3]

for i in range(5):
  try:
      print(data[i])
  except IndexError as e:
    print(e)
    break
















