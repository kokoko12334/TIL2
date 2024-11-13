import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

g = defaultdict(list)
for _ in range(m):
    a, b = [int(i) for i in input().split()]
    g[a].append(b)
    g[b].append(a)

answer = 0
seen = [0] * n
def dfs(node, cnt):
    global answer

    if cnt == 5 or answer == 1:
        answer = 1
        return

    for i in g[node]:
        if seen[i] == 1:
            continue
        seen[i] = 1
        dfs(i, cnt+1)
        seen[i] = 0

for i in range(n):
    seen[i] = 1
    dfs(i, 1)
    if answer:
        break
    seen[i] = 0

print(answer)