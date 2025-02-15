n = int(input())

m = []
for _ in range(n):
    x, y = [float(i) for i in input().split()]
    m.append((x, y))

g = [[0] * n for _ in range(n)]
arr = []
for i in range(n):
    x1, y1 = m[i]
    for j in range(i+1, n):
        x2, y2 = m[j]
        
        dis = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
        g[i][j] = dis
        g[j][i] = dis
        arr.append((dis, i, j))


arr.sort(key = lambda x: x[0])
def initialize(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank


parent, rank = initialize(n)

def find(idx):
    if parent[idx] != idx:
        parent[idx] = find(parent[idx])
    return parent[idx]

def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    rank[a] += rank[b]


answer = 0
for i in range(len(arr)):
    dis, x, y = arr[i]

    xroot = find(x)
    yroot = find(y)

    if xroot != yroot:
        answer += dis
        union(x, y)

print("{:.2f}".format(answer))