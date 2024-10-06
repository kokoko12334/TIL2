
import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]

parent = [i for i in range(n+1)]
rank = [0]*(n+1)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(x,y,parent,rank):
    xroot = find(parent, x)
    yroot = find(parent,y)

    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

for _ in range(m):
    c,a,b = [int(i) for i in input().split()]
    if c == 0:
        union(a,b,parent,rank)
    else:
        aroot = find(parent, a)
        broot = find(parent,b)
        if aroot == broot:
            print("YES")
        else:
            print("NO")







