#파이썬에서는 제너레이터의 코루틴과 구분하기 위해서 asynio의 코루틴을 네이티브 코루틴이라고 함



# 이벤트 루프는 비동기 코드의 실행을 관리하고, 여러 개의 코루틴이나 태스크를 비동기적으로 실행하며, 
# 비동기 이벤트를 처리하는 중심 역할을 수행합니다. 
# 이벤트 루프는 코루틴을 스케줄링하고, 이벤트 발생 시 해당 이벤트 핸들러를 호출하며, 비동기 코드의 실행 흐름을 제어합니다.

# 파이썬에서 비동기 처리는 주로 async/await 키워드를 사용하여 구현되며, 비동기 이벤트 루프는 이러한 비동기 코드를 실행하고 관리합니다. 
# 이벤트 루프는 다양한 비동기 작업을 병렬로 실행하고, 
# 각 작업이 I/O 작업이나 다른 비동기 작업의 완료를 기다리는 동안 다른 작업을 수행할 수 있도록 해줍니다.

# 간단한 비동기 처리 예시에서는 asyncio.run() 함수를 사용하여 이벤트 루프를 생성하고 실행하는데, 
# loop.run_until_complete()를 사용할 수도 있습니다. 이벤트 루프를 사용함으로써 비동기 코드의 실행을 관리하고 제어할 수 있게 됩니다.
import asyncio

async def hello(): # async def로 코루틴 객체 생성
    
    print("hello1")
    await asyncio.sleep(4)
    print("world1")

async def hello2(): # async def로 코루틴 객체 생성
    
    print("hello2")
    await asyncio.sleep(4)
    print("world2")
loop = asyncio.get_event_loop() # 이벤트 루프 생성
loop.run_until_complete(hello()) 
loop.close() #이벤트 루프 닫음
asyncio.run(hello())   # async def가 혼자라면 단순하게 이걸로 처리 가능
asyncio.run(hello2())   # async def가 혼자라면 단순하게 이걸로 처리 가능

async def main():
    task = [hello(),hello2()]
    await asyncio.gather(*task)
asyncio.run(main()) # 서로 다른 작업을 수행하려면 그 서로 다른 작업도 비동기로 구현해야하는 듯

# await 뒤에는 태스크,코루틴,퓨처 객체만 올 수 있다.
# 코루틴 안에서의 작업들은 비동기가 아니다. 여러개의 태스크를 실행시켜 놓음=> 즉 서로 다른 코루틴간의 실행이 비동기가 된다.
async def add(a,b,time): #기다리는데 1초 걸리는 작업
    print("add: {0} + {1}".format(a,b))
    await asyncio.sleep(time)
    return a+b


async def print_add(a,b,time):
    tasks = [add(a,b,time), add(a,b,time+1),add(a,b,time+2)]   # 여러개의 task(비동기 작업)를 지정하고
    # result = await add(a,b)
    result = await asyncio.gather(*tasks)  # 결과 처리가 "전부 완료" 되면 결과 값을 리스트로 반환
    print("print_add:{0}".format(result))



# asyncio.run(print_add(1,2,3))
# print("기타작업")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_add(1,2,3))
# loop.close()


# 태스크, 코루틴, 퓨처객체는 비동기작업을 지칭하지만 세세한 차이가 있는 듯
# 코루틴 => 퓨처(코루틴에서 기능 추가=> 비동기 작업의 현재상황) => 태스크(퓨처에서 더 기능 추가+ 상태확인 및 취소 가능)


# async def compute_square(num):
#     await asyncio.sleep(1)
#     result = num**2
#     return result

# #future
# #future 객체를 생성하고 future객체안에 set_result를 설정하고 그 다음을 진행한다.
# async def main_future():
#     future = asyncio.Future()

#     async def set_result():
#         result = await compute_square(5)
#         future.set_result(result)

#     asyncio.create_task(set_result())


#     if not future.done():
#         print("future is not done yet.")
    
#     result = await future
#     print(f"result:{result}")

# asyncio.run(main_future())

# # future 객체를 생성해서 하는 것보다 더 간단하게 수행이 가능하다.
# # => 비동기 작업을 바로 creata_task로 생성하고 이를 바로 실행한다.
# async def main_task():
#     task = asyncio.create_task(compute_square(5))

#     if not task.done():
#         print("task is not done yet.")
#     result = await task
#     print(f"result:{result}")
# asyncio.run(main_task())





