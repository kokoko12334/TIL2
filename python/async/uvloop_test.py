
# #uvloop는 asyncio의 이벤트 루프를 더 빠르게 만들어주는 외부 라이브러리입니다.
# #uvloop는 c로 만들어짐.
# import asyncio
# import uvloop  #window에서는 안되는듯

# async def hello():
#     print("hello1")
#     await asyncio.sleep(4)
#     print("world1")

# # uvloop의 이벤트 루프를 사용하여 생성
# loop = uvloop.new_event_loop()
# asyncio.set_event_loop(loop)

# # 이벤트 루프를 통해 코루틴 실행
# loop.run_until_complete(hello())

# # 이벤트 루프를 닫음
# loop.close()