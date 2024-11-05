def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    seen = [0] * n
    
    def dfs(cnt):
        nonlocal answer, k
        
        answer = max(cnt, answer)
        
        for i in range(n):
            if seen[i]:
                continue
            need, cost = dungeons[i]
            if k < need:
                continue
        
            k -= cost
            seen[i] = 1
            dfs(cnt+1)
            seen[i] = 0
            k += cost
    
    dfs(0)
    return answer