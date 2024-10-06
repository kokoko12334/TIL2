from collections import deque
def solution(stones, k):
    
    n = len(stones)
    q = deque()
    l, r = 0, 0 
    answers = []
    while r < n:
        while q and stones[q[-1]] < stones[r]:
            q.pop()
        q.append(r)
        
        if l > q[0]:
            q.popleft()
        
        if r+1 >= k:
            answers.append(stones[q[0]])
            l += 1
            
        r += 1
    answer = min(answers)
    
    return answer