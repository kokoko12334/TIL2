def my_generator():
    print("Start")
    yield 1
    print("Resume")
    yield 2
    print("End")

gen = my_generator()

# 첫 번째 next() 호출
print(next(gen))  # 출력: Start, 값: 1

# 두 번째 next() 호출
print(next(gen))  # 출력: Resume, 값: 2

# 세 번째 next() 호출
print(next(gen))  # 출력: End, StopIteration 예외 발생


import inspect

# 제너레이터 객체의 내부를 살펴봅니다.
print(inspect.getgeneratorstate(gen))  # 출력: GEN_CLOSED