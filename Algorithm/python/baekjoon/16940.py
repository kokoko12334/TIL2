import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

g = defaultdict(list)
for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    g[a].append(b)
    g[b].append(a)

path = [int(i) for i in input().split()]

q = deque([(1,1)])
seen = [0] * (n+1)
seen[1] = 1
layer = defaultdict(set)
find_key = [0] * (n+1)
global_cnt = 0
while q:
    node, cnt = q.popleft()
    global_cnt += 1
    find_key[global_cnt] = cnt
    layer[cnt].add(node)
    for i in g[node]:
        if seen[i] == 0:
            seen[i] = 1
            q.append((i, cnt+1))

answer = 1
for i in range(n):
    num = path[i]
    key_ = find_key[i+1]
    lst = layer[key_]
    if num not in lst:
        answer = 0
        break

print(answer)
