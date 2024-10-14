import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
entry = [0] * (n+1)

g = defaultdict(list)
for _ in range(m):
    node1, node2 = [int(i) for i in input().split()]
    entry[node2] += 1
    g[node1].append(node2)


hq = []
for i in range(1, n+1):
    if entry[i] == 0:
        heappush(hq, i)

answer = []
while hq:
    num = heappop(hq)
    answer.append(num)

    for next_ in g[num]:
        entry[next_] -= 1
        if entry[next_] == 0:
            heappush(hq, next_)

print(*answer)
