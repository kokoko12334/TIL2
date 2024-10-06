import sys
sys.setrecursionlimit(10**5)

# 루트노드부터 시작하여 깊이를 구하는 함수
def dfs(now, depth):
    c[now] = True
    d[now] = depth

    for next_ in graph[now]:
    	# 깊이를 이미 구한 경우 무시
        if c[next_]:
            continue
        parent[next_] = now
        dfs(next_, depth+1)


def lca(a, b):
    # 두 노드의 깊이가 다를 경우
    while d[a] != d[b]:
    	# 깊이가 큰 노드가 부모 노드로 이동
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 깊이는 같지만 두 노드가 서로 다를 경우
    while a != b:
    	# 두 노드를 부모 노드로 이동
        a = parent[a]
        b = parent[b]
    return a


n = int(input())
arr = []
maxN = 0
for _ in range(n-1):
    x, y = map(int, input().split())
    arr.append([x, y])
    maxN = max(maxN, max([x, y]))

graph = [[] for _ in range(maxN+1)]
for x, y in arr:
    graph[x].append(y)
    graph[y].append(x)

parent = [0] * (maxN + 1)
d = [0] * (maxN + 1)
c = [0] * (maxN + 1)

dfs(1, 0) # 루트노드 1 깊이는 0
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))