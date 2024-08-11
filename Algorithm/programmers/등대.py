from collections import defaultdict
def solution(n, lighthouse):
    
    g = defaultdict(list)
    for i in range(n-1):
        n1, n2 = lighthouse[i]
        g[n1].append(n2)
        g[n2].append(n1)
    
    dp = [[0, 1] for _ in range(n+1)]
    seen = [0] * (n+1)
    
    def dfs(node, turn):
        
        
        
        for next_node in g[node]:
            if seen[next_node] == 0:
                seen[next_node] = 1
                dp[node][0] += dfs(next_node, 1)
                dp[node][1] += min(dfs(next_node, 0), dfs(next_node, 1)) + 1
                seen[next_node] = 0
    
        return dp[node][turn]
    
    seen[1] = 1
    dfs(1,0)
    dfs(1,1)
    for i in dp:
        print(i)
    answer = 0
    return answer