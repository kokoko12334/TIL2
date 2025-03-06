# from itertools import combinations
import sys
sys.setrecursionlimit(10**6)
def solution(n, q, ans):
    answer = 0
    m = len(ans)
    
    # subs = list(combinations([i for i in range(1, n+1)], 5))
    

    def recur(left):
        nonlocal n

        if len(arr) == 5:
            subs.append(set(arr))
            return
        
        for i in range(left, n + 1):
            arr.append(i)
            recur(i + 1)
            arr.pop()
    subs = []
    arr = []
    recur(1)
    

    def check(nums):
        nonlocal m
        for i in range(m):
            cnt = 0
            for num in q[i]:
                if num in nums:
                    cnt += 1
            if cnt != ans[i]:
                return False
        
        return True
            
    for nums in subs:
        if check(nums):
            answer += 1
    
    return answer