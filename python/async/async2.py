import asyncio
#먼저 async with은 클래스나 함수를 비동기로 처리한 뒤 결과를 반환하는 문법입니다. 
#그리고 async for는 비동기로 반복하는 문법입니다.

#async with은 with 다음에 클래스의 인스턴스를 지정하고 as 뒤에 결과를 저장할 변수를 지정합니다.

# async with으로 동작하는 클래스를 만들려면 __aenter__와 __aexit__ 메서드를 구현해야 합니다(asynchronous enter, asynchronous exit라는 뜻). 
# 그리고 메서드를 만들 때는 반드시 async def를 사용합니다.


class AsyncAdd:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    async def __aenter__(self):
        await asyncio.sleep(1)
        return self.a + self.b # __aenter__에서 리턴값이 as에 지정한 변수에 전달
    
    #__aexit__ 메서드는 async with as를 완전히 벗어나면 호출되는데 여기서는 특별히 만들 부분이 없으므로 
    # pass를 넣습니다(메서드 자체가 없으면 에러가 발생합니다).
    async def __aexit__(self, exc_type, exc_value, traceback):
        pass
    

async def main():
    async with AsyncAdd(1,2) as result:  #AyncAdd 에서 정의된 __aenter__를 실행해서 결과값을 result에 저장
        print(result)

# asyncio.run(main())



# 이번에는 async for입니다. async for로 동작하는 클래스를 만들려면 __aiter__와 __anext__ 메서드를 구현해야 합니다(asynchronous iter, asynchronous next라는 뜻). 
# 그리고 메서드를 만들 때는 반드시 async def를 사용합니다.


class AsyncCounter:
    def __init__(self,stop):
        self.current = 0
        self.stop = stop
    
    def __aiter__(self):
        return self
    

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1)
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

async def main():
    async for i in AsyncCounter(3):
        print(i,end=" ")

# asyncio.run(main())


#제너레이터로 구현

async def async_counter(stop):
    n = 0
    while n <stop:
        yield n
        n += 1
        await asyncio.sleep(1.0)

async def main():
    async for i in async_counter(3):
        print(i)

# asyncio.run(main())



# await를 이용하여 코루틴을 비동기 실행 가능
async def async_one():
    await asyncio.sleep(1)
    return 1
 
async def main():
    coroutines = [async_one, async_one, async_one]
    a = [await co() for co in coroutines]
    print(a)    # [1, 1, 1]

asyncio.run(main())