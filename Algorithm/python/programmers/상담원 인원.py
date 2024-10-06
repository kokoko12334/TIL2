from collections import deque
from itertools import combinations, product
from heapq import *

def solution(k, n, reqs):
    
    
    sch = {i:[] for i in range(1,k+1)}
    
    
    for r in reqs:
        s,e,t = r
        sch[t].append([s,e])
    
    
    cases = list(combinations(range(n-1),k-1))
    
    answer = float("inf")
    for c in cases:
        tutors = {i: 1 for i in range(1,k+1)}
        arr = deque([0]*(n-1))
        for i in c:
            arr[i] = 1
        
        
        #cases분류
        t = 1
        cnt = 0
        while arr:
            val = arr.popleft() 
            if val == 0:
                cnt += 1
            else:
                tutors[t] += cnt
                t += 1
                cnt = 0
        if cnt:
            tutors[t] += cnt
        
        result = 0
        for k,arr_v in sch.items():
            nn = tutors[k]
            arr2 = []
            for v in arr_v:
                s,e = v
                if len(arr2) < nn:
                    heappush(arr2,s+e)
                else:
                    minn = heappop(arr2)
                    diff = minn - s
                    if diff > 0:
                        result += diff
                    heappush(arr2,max(s,minn)+e)
        
        answer = min(result,answer)
                    
    return answer