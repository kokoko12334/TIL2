from heapq import heappush, heappop
def solution(n, works):
    
    hq = []
    for i in range(len(works)):
        heappush(hq, -works[i])
    
    while n:
        num = -heappop(hq)
        if num == 0:
            break
        num -= 1
        n -= 1
        heappush(hq, -num)
    # print(hq)
    answer = sum([num**2 for num in hq])
    return answer