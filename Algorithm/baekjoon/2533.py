from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)
for _ in range(n-1):
    u, v = [int(i) for i in input().split()]
    tree[u].append(v)
    tree[v].append(u)


dp = [[0] * (n+1) for _ in range(2)]
seen = [0] * (n+1)
def dfs(node):

    seen[node] = 1
 
    for chil in tree[node]:
        if not seen[chil]:
            dfs(chil)
            dp[0][node] += dp[1][chil]
            dp[1][node] += min(dp[0][chil], dp[1][chil])
    
    dp[1][node] += 1


dfs(1)
answer = min(dp[0][1], dp[1][1])
print(answer)