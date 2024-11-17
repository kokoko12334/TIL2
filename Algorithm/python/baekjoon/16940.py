import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

g = defaultdict(set)
for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    g[a].add(b)
    g[b].add(a)

path = [int(i) for i in input().split()]
answer = 1
if path[0] != 1:
    answer = 0
else:
    seen = set()
    seen.add(1)
    order = deque()
    next_node = g[1]
    for i in range(1, n):
        if not next_node:
            next_node = order.popleft()
        num = path[i]
        if num in next_node:
            next_node.remove(num)
            seen.add(num)
            add_node = g[num] - seen
            if add_node:
                order.append(g[num] - seen)
        else:
            answer = 0
            break


print(answer)




