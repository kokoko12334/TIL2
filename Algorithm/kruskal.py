def initialize(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]
    
def union(x, y, parent, rank):
    xroot = find(x, parent)
    yroot = find(y, parent)

    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


#A:0, B:1, C:2, D:3, E:4, F:5
g = [
[0,6,2,2,0,0],
[6,0,0,0,0,3],
[2,0,0,0,2,0],
[2,0,0,0,1,1],
[0,0,2,1,0,0],
[0,3,0,1,0,0]
]

n = 6
parent, rank = initialize(n)
seen = [[0]*n for _ in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        if g[i][j] and not seen[i][j] and not seen[j][i]:
            arr.append((i, j, g[i][j]))
            seen[i][j] = 1
            seen[j][i] = 1

arr.sort(key=lambda x: -x[2])
arr

edge = 0
result = []
while edge < n-1:
    i, j, num = arr.pop()
    
    # 싸이클 여부 확인
    root_i = find(i, parent)
    root_j = find(j, parent)
    if root_i == root_j:
        continue
    
    union(i, j, parent, rank)
    result.append((i, j, num))
    edge += 1
    

#a:0, b:1, c:2, d:3, e:4, f:5
result