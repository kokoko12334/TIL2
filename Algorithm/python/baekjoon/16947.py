import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

g = defaultdict(list)
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    g[a].append(b)
    g[b].append(a)


def dfs(start, parent, node):
    
    for next_node in g[node]:
        if next_node == parent:
            continue

        if next_node == start:
            return True    

        if seen[next_node]:
            continue
        
        seen[next_node] = 1
        result = dfs(start, node, next_node)
        if result:
            return True
        seen[next_node] = 0

cycle = set()
for node in range(1, n+1):
    seen = [0] * (n + 1)
    seen[node] = 1
    if dfs(node, -1, node):
        cycle.add(node)

answer = [0] * (n + 1)

no_cycle = set(range(1, n+1)) - cycle


for start in no_cycle:
    seen = [0] * (n + 1)
    q = deque([(start, 0)])
    seen[start] = 1
    while q:
        node, cnt = q.popleft()
        for next_node in g[node]:
            if seen[next_node]:
                continue

            if next_node in cycle:
                answer[start] = cnt + 1
                break
            seen[next_node] = 1
            q.append((next_node, cnt + 1))


print(*answer[1:])