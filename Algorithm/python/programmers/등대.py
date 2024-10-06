import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    
    g = defaultdict(list)
    for i in range(n-1):
        n1, n2 = lighthouse[i]
        g[n1].append(n2)
        g[n2].append(n1)
    
    dp = [[0, 1] for _ in range(n+1)]
    seen = [0] * (n+1)
    
    def dfs(node):
        seen[node] = 1
        for next_node in g[node]:
            if not seen[next_node]:
                off, on = dfs(next_node)
                dp[node][0] += on
                dp[node][1] += min(off, on)
    
        return dp[node][0], dp[node][1]
    dfs(1)
    
    return min(dp[1][0], dp[1][1])