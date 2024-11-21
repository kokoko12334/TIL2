import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, k = [int(i) for i in input().split()]
INF = float('inf')
g = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    g[a][b] = c


def dij(node):
    distances = [[] for _ in range(n+1)]
    seen = [0] * (n+1)
    distances[node].append(0)
    q = []
    heappush(q, (0, node))

    while q:
        current_dis, current_node = heappop(q)

        if seen[current_node] == k:
            continue

        seen[current_node] += 1

        for i in range(n+1):
            dis = g[current_node][i]
            if dis != INF and seen[i] < k:
                new_dis = current_dis + dis
                distances[i].append(new_dis)
                heappush(q, (new_dis, i))

    return distances                


res = dij(1)

for i in range(1, n+1):
    arr = res[i]
    arr.sort()
    if len(arr) < k:
        print(-1)
    else:
        print(arr[k-1])