

# 비선점형 => 자원(cpu)을 뺏어올 수 있다.
# 선점형 => 자원(cpu)을 뺏어올 수 없다.
#코루틴 => 비선점=>
#동시성, 병행성(concurrency) => 하나의 자원이 왓다 갓다, 
#병렬성(parallelism) => 여러개의 자원을 동시에 수행


#main routine=> sub routine, 주종관계 sub routine은 무조건 단독 실행이 x main routine에 의해서만 실행가능
# coroutine은 그런 관계 아님 서로가 서로 호출 가능, 서로 대등한 관계


# 코루틴안에 값전달
def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함,여기서 제어권 넘김
        print(x)
 
 
co = number_coroutine()

#코루틴객체.send(None)과 같이 send 메서드에 None을 지정해도 코루틴의 코드를 최초로 실행할 수 있습니다.

next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)

co.send(None)

co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄



# 코루틴에서 바깥으로 값 전달
def sum_coroutine():
    total = 0
    while True:
        x = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x
 
co = sum_coroutine()
print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
 
print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력



# 코루틴 종료


def number_coroutine():
    while True:
        x = (yield)
        print(x)
 
co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()    # 코루틴 종료



# 코루틴 close 하면 GenreatorExit 예외 발생시킴
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')


co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()


# 코루틴 예외발생시 값 전달하면서 종료
def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total    # 코루틴 바깥으로 값 전달
 
co = sum_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
print(co.throw(RuntimeError, '예외로 코루틴 끝내기')) # 190
                                                    # 코루틴의 except에서 yield로 전달받은 값



