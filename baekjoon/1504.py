from heapq import *
import sys
input = sys.stdin.readline
n,e = [int(i) for i in input().split()]

g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(e):
    v1,v2,c = [int(i) for i in input().split()]
    g[v1][v2] = c
    g[v2][v1] = c

v1,v2 = [int(i) for i in input().split()]

hq = []
heappush(hq, (0,1))
dp1 = [float("inf")]*(n+1)
dp1[1] = 0
while hq:
    d,s = heappop(hq)
    for i in range(n+1):
        if not g[s][i]:
            continue
        cost = d + g[s][i]
        if cost < dp1[i]:
            dp1[i] = cost
            heappush(hq,(cost,i))

hq = []
heappush(hq, (0,v1))
dp_v1 = [float("inf")]*(n+1)
dp_v1[v1] = 0
while hq:
    d,s = heappop(hq)
    for i in range(n+1):
        if not g[s][i]:
            continue
        cost = d + g[s][i]
        if cost < dp_v1[i]:
            dp_v1[i] = cost
            heappush(hq,(cost,i))


hq = []
heappush(hq, (0,v2))
dp_v2 = [float("inf")]*(n+1)
dp_v2[v2] = 0
while hq:
    d,s = heappop(hq)
    for i in range(n+1):
        if not g[s][i]:
            continue
        cost = d + g[s][i]
        if cost < dp_v2[i]:
            dp_v2[i] = cost
            heappush(hq,(cost,i))


answer1 = 0
answer2 = 0

if dp1[v1] != float("inf") and dp_v1[v2]!= float("inf") and dp_v2[n]!= float("inf"): 
    answer1 = dp1[v1] + dp_v1[v2] + dp_v2[n]

if dp1[v2]!= float("inf") and dp_v2[v1]!= float("inf") and dp_v1[n]!= float("inf"):
    answer2 = dp1[v2] + dp_v2[v1] + dp_v1[n]

if answer1 and answer2:
    print(min(answer1, answer2))
elif answer1 and not answer2:
    print(answer1)
elif answer2 and not answer1:
    print(answer2)
else:
    print(-1)
