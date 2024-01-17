import sys
input = sys.stdin.readline
t = int(input())

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(y,x,parent,rank):
    xroot = find(parent,x)
    yroot = find(parent,y)

    if yroot == xroot:
        return
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
        freinds[yroot] += freinds[xroot]
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        freinds[xroot] += freinds[yroot]
    else:
        parent[xroot] = yroot
        rank[yroot] += 1
        freinds[yroot] += freinds[xroot]

for _ in range(t):
    f = int(input())
    check = set()
    freinds = dict()
    rank = dict()
    parent = dict()
    for _ in range(f):
        a,b = input().split()
        if a not in check:
            parent[a] = a
            rank[a] = 0
            freinds[a] = 1
            check.add(a)
        if b not in check:
            parent[b] = b
            rank[b] = 0
            freinds[b] = 1
            check.add(b)
        
        union(a,b,parent,rank)
        
        aroot = find(parent, a)
        print(freinds[aroot])
