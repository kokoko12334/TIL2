
#cooperative routine


def add(a,b):
    c= a+b
    print(c)
    print('add')

def calc():
    add(1,2)
    print('calc')

calc()         #add함수를 실행하고 그다음에 calc함수로 돌아옴(실행함 print(calc)를 말함.)
#이때 이 둘의 관계를 calc()는 메인루틴, add(a,b)는 서브루틴이라고 함. 이는 종속 관계임 즉, 서브루틴->메인루틴으로 돌아감
#이때 종속가 아닌 동등한 관계를 코루틴이라고 함 즉 루틴1-> 루틴2-> 루틴1-> 루틴2 .... 처럼 계속 실행 가능함.




#코루틴에 값 보내기
def number_coroutine():
    while True:                #계속 루틴을 반복하므로 while True를 사용
        x = (yield)          #밖에서 값을 받아냄 이때 코루틴은 yield의 특수한 형태이고 ()를 써야함.
        print(x)

co = number_coroutine()         #함수 할당
next(co)                     #코루틴의 최초실행
co.send(None)            #None을 써도 최초로 실행이 됨.


co.send(1)       #코루틴에 1을 보냄 이때 .send()를 씀
co.send(2)
co.send(3)




#코루틴 바깥으로 값 전달하기 코딩도장 41.2부터임 여긴 여러워서 일단 생략








































