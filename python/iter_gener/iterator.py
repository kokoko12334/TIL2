from collections.abc import Iterable, Iterator, Generator



## 이터레이터
lst = [1,2,3]
print(isinstance(lst,Iterable)) # 반복가능한 객체
print(isinstance(lst,Iterator)) # 이터레이터 그자체는 아님

#iterator 타입으로 지정
lst_iter = lst.__iter__()
lst_iter = iter(lst)
print(isinstance(lst_iter,Iterator))

#next를 이용하여 다음 값들을 차례대로 반환
#그래서 for문도 이터러블 객체를 이터레이터로 만들고 next를 StopIteration까지 호출함
try:
    while True:
        # i = lst_iter.__next__()
        i = next(lst_iter)
        print(i)
        print("dsadad")
except StopIteration as e:
    pass



##제너레이터: 이터레이터를 간단한 방식으로 구현, 이터레이터를 생성해주는 함수
# 반환값을 return대신 yield를 쓰며, yield는 반환을 하고, 제어권을 넘겨준다.
def gener():
    yield 1
    yield 2

isinstance(gener(),Generator)

gener1 = gener()

for _ in range(3):
    print(next(gener1))


#응용
    
def ge1(n):
    for i in range(1,n+1):
        yield i*i

#혹은 다음과 같이 컴프리헨션 스타일로 표현가능
n = 5
g = (i*i for i in range(1,n+1))

g = ge1(5)
next(g)  

##활용

import time


def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"
# iterator는 함수를 다 실행하고 반환값을 다 반환
list_job = iter([longtime_job() for i in range(5)])

print(next(list_job))


#제너레이터는 원하는 때만 longtime_job()을 실행시키고 반환값을 반환

def job_gener():
    for i in range(5):
        print(f"job start{i}")
        time.sleep(1)
        yield "done"
list_job = job_gener()
# list_job = (longtime_job() for i in range(5))
print(next(list_job))


#즉, 모든 함수를 한꺼번에 실행하는 것이 아니라 필요할 때만 실행하는 방식으로 바뀌게 된다.
# 이러한 방식을 '느긋한 계산법(lazy evaluation)'이라 부른다.시간이 오래 걸리는 작업을 한꺼번에 처리하기보다는 필요한 경우에만 호출하여 사용할 때 제너레이터는 매우 유용하다.
# 내가 코딩의 흐름을 통제할 수 있다 =>?


