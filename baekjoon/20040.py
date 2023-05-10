import sys
input = sys.stdin.readline
n, m = [int(i) for i in input().split()]
parent = [i for i in range(n)]
rank = [0]*n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(y,x):
    xroot = find(x)
    yroot = find(y)

    if xroot == yroot:
        return
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[xroot] = yroot
        rank[yroot] += 1
flag = True
answer = 0
for cnt in range(m):
    
    n1,n2 = [int(i) for i in input().split()]
    if flag:
        if find(n1) == find(n2):
            answer = cnt + 1
            flag = False

        union(n1,n2)

print(answer)

