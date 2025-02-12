n = int(input())

starts = []
for _ in range(n):
    y, x = [float(i) for i in input().split()]
    starts.append([y, x])

g = [[0] * n for _ in range(n)]

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

