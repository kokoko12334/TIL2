import sys
from collections import defaultdict, deque
input = sys.stdin.readline

t = int(input())

def bfs(q, target):
    global n

    seen = [0] * n
    for i in range(len(q)):
        node, cnt = q[i]
        seen[node] = cnt

    while q:
        node, cnt = q.popleft()
        for next_node in g[node]:
            cnt_arr[next_node] -= 1
            seen[next_node] = max(seen[next_node], cnt)
            if cnt_arr[next_node] == 0:
                seen[next_node] += arr[next_node]
                q.append((next_node, seen[next_node]))
    # print(seen)
    return seen[target]
    
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    g = defaultdict(list)
    
    cnt_arr = [0] * n

    for _ in range(k):
        a, b = [int(i) - 1 for i in input().split()]
        g[a].append(b)
        cnt_arr[b] += 1

    target = int(input()) - 1

    q = deque()
    for i in range(n):
        if cnt_arr[i] == 0:
            q.append((i, arr[i]))

    result = bfs(q, target)
    print(result)


