import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

g = defaultdict(list)
for _ in range(n):
    data = [int(i) for i in input().split()]
    p = data[0]
    data = data[1:-1]
    for i in range(0, len(data)-1, 2):
        ch = data[i]
        cost = data[i+1]
        g[p].append((ch, cost))


def dfs(node, dis):
    global v1, result

    if result < dis:
        v1 = node
        result = dis


    
    for i in g[node]:
        next_node, cnt = i
        if next_node not in seen:
            seen.add(next_node)
            dfs(next_node, dis + cnt)
            seen.remove(next_node)
    
    return

v1 = 1
result = 0
seen = set()
seen.add(1)
dfs(1, 0)
seen.remove(1)



start = v1
v1 = 0
result = 0
seen.add(start)
dfs(start, 0)
seen.remove(start)
print(result)



