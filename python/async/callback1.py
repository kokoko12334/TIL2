import asyncio

async def my_coroutine():
    print("My coroutine has started.")
    await asyncio.sleep(3)  # 비동기적으로 3초 동안 대기
    print("My coroutine has finished.")
    return 'Coroutine Result'

def my_callback(future):
    # 콜백 함수는 future 객체를 인자로 받습니다.
    print("Callback: got the result -", future.result())

async def main():
    # 코루틴을 스케줄링하고 Task 객체를 얻습니다.
    task = asyncio.create_task(my_coroutine())
    
    # Task가 완료되면 호출될 콜백 함수를 추가합니다.
    task.add_done_callback(my_callback)
    
    # Task의 완료를 기다립니다.
    await task

# 이벤트 루프를 실행합니다.
asyncio.run(main())