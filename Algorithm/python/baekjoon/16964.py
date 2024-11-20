import sys
from collections import defaultdict
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
    next_ = g[1] - set()
    seen = set()
    seen.add(1)
    orders = []
    for i in range(1, n):
        num = path[i]
        if not next_ and orders:
            next_ = orders.pop()
        
        if num not in next_:
            answer = 0
            break
        else:
            next_.remove(num)
            if next_:
                orders.append(next_)
            seen.add(num)
            next_ = g[num] - seen

print(answer)
