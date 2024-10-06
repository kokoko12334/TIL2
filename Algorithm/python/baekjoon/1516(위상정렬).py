from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
g_in = {i:0 for i in range(1,n+1)}
g = {i:[] for i in range(1,n+1)}
lst = []
check = {i:[] for i in range(1,n+1)}
for i in range(1,n+1):
    a = [int(i) for i in input().split()]
    dp[i] = a[0]
    idx = 1
    while a[idx] != -1:

        g[a[idx]].append(i)
        check[i].append(a[idx])
        g_in[i] += 1
        idx += 1


q = deque()
seen = [0]*(n+1)
for k,v in g_in.items():
    if not v:
        q.append(k)
        seen[k] = 1
while q:
    out = q.popleft()
    
    for i in g[out]:
        if not seen[i]:
            g_in[i] -= 1
            if not g_in[i]:
                dp[i] += max([dp[k] for k in check[i]])
                
                q.append(i)
                seen[i] = 1

for i in dp[1:]:
    print(i)