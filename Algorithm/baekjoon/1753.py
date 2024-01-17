import sys
from heapq import *
input = sys.stdin.readline
v,e = [int(i) for i in input().split()]
s = int(input())
g = {i:[] for i in range(v+1)}
for _ in range(e):
    d,e,c = [int(i) for i in input().split()]
    g[d].append([e,c])
    

hq = []
heappush(hq,(0,s))
dp = [float("inf")]*(v+1)
dp[s] = 0

while hq:
    d, x = heappop(hq)
    if dp[x] <d:
        continue
    for i in g[x]:
        node, dd = i
        cost = dd + d
        if cost < dp[node]:
            dp[node] = cost
            heappush(hq, (cost,node))

for i in dp[1:]:
    if i == float("inf"):
        print("INF")
    else:
        print(i)