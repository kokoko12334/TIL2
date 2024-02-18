from time import time, sleep
from urllib.request import Request, urlopen
import asyncio
from concurrent.futures import ProcessPoolExecutor
# # 동기로 처리 
# urls = ['https://www.google.co.kr/search?q=' + i
#         for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]
 
# begin = time()
# result = []
# for url in urls:
#     request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})    # UA가 없으면 403 에러 발생
#     response = urlopen(request)
#     page = response.read()
#     result.append(len(page))
 
# print(result)
# end = time()
# print('실행 시간: {0:.3f}초'.format(end - begin))



##비동기로 작성
#우선 ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']의 웹페이지를 가져오는 식이 비동기 작업임.

async def async_req(request: Request):
    process_executor = ProcessPoolExecutor()
    # None이면 ThreadPoolExecutor   process_executor는 프로세스
    #ThreadPoolExecutor는 I/O 바운드 작업에 적합하며, ProcessPoolExecutor는 CPU 바운드 작업에 적합합니다.executor를 직접 지정하려면 적절한 상황에서 선택하면 됩니다.
    response = await loop.run_in_executor(None, urlopen, request)   #loop.run_in_executor는 블록킹작업을 다른 스레드에서 병렬로 실행시킴
    # page = await loop.run_in_executor(None,response.read)
    page = response.read()
    return len(page)
    

async def main():
    
    urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]
    
    tasks = [async_req(Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})) for url in urls]
    
    result = await asyncio.gather(*tasks)
    print(result)


begin = time()
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
loop.close()  
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))




# def blocking_function():
#     # 어떤 블로킹 작업을 수행
#     return "Done"

# async def async_function():
#     loop = asyncio.get_event_loop()
    
#     # loop.run_in_executor를 사용하여 블로킹 함수를 비동기적으로 실행
#     result = await loop.run_in_executor(None, blocking_function)
    
#     print(result)

# asyncio.run(async_function())


