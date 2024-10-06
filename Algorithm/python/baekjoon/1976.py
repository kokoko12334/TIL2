import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n)]
rank = [0]*n
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    
    return parent[x]

def union(x,y,parent,rank):
    xroot = find(parent,x)
    yroot = find(parent,y)
    if xroot == yroot:
        return
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot]  = xroot
    else:
        parent[xroot] = yroot
        rank[yroot] += 1
    
for i in range(n):
    lst = [int(j) for j in input().split()]
    for j in range(n):
        if lst[j]:
            union(i,j,parent, rank)

plan = [int(i)-1 for i in input().split()]
plan = list(set(plan))

nn = len(plan)
flag = True
for i in range(nn):
    if flag:
        for j in range(i,nn):
            x = plan[i]
            y = plan[j]
            xroot = find(parent,x)
            yroot = find(parent,y)
            if xroot != yroot:
                flag = False
                break
if flag:
    print("YES")
else:
    print("NO")