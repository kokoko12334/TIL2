import heapq

t = int(input())

def go(arr):
    
    answer = 0
    heapq.heapify(arr)

    while arr:

        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        result = a+b
        answer += result
        if arr:
            heapq.heappush(arr,result)
     
    return answer



for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(go(arr))

