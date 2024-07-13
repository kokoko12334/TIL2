import sys
from collections import deque
#https://www.acmicpc.net/problem/18243
input = sys.stdin.readline

n, k = [int(i) for i in input().split()]
g = [[] for _ in range(n+1)]
for _ in range(k):
    n1, n2 = [int(i) for i in input().split()]
    g[n1].append(n2)
    g[n2].append(n1)

visited = [0] * (n+1)
result = True
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    q = deque([(i,0)])
    while q:
        node, cnt = q.popleft()

        if cnt > 6:
            result = False
            break
        for i in g[node]:
            if not visited[i]:
                q.append((i,cnt + 1))
                visited[i] = 1
    if sum(visited) != n:
        result = False

    if not result:
        break

if result:
    print("Small World!")
else:
    print("Big World!")