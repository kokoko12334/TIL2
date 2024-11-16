import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

INF = float('inf')
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    edges.append((a, b, c))


def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur, next_node, cost = edges[j]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost

                if i == n - 1:
                    return True                

    return False

cycle = bf(1)

if cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])

