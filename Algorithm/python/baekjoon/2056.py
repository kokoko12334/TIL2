import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

start_time = [0] * (n+1) #최대값
in_cnt = [0] * (n+1)
cost = [0] * (n+1)
g = defaultdict(list)

for i in range(1, n+1):
    inputs = [int(i) for i in input().split()]
    cost[i] = inputs[0]
    for j in range(2, 2+inputs[1]):
        g[inputs[j]].append(i)
        in_cnt[i] += 1

q = deque()
for i in range(1, n+1):
    if in_cnt[i] == 0:
        q.append(i)

answer = 0
while q:
    number = q.popleft()
    start = start_time[number]
    end = start + cost[number]
    answer = max(answer, end)
    for next_ in g[number]:
        start_time[next_] = max(end, start_time[next_])
        in_cnt[next_] -= 1
        if in_cnt[next_] == 0:
            q.append(next_)

print(answer)