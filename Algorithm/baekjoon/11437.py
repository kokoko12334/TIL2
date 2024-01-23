import sys

input = sys.stdin.readline

n = int(input())

tree = {}

for _ in range(n-1):
    a,b = [int(i) for i in input().split()]

    if a not in tree:
        tree[a] = [b]
    else:
        tree[a].append(b)
    if b not in tree:
        tree[b] = [a]
    else:
        tree[b].append(a)
    


stack = [[1,0]]
parent = [i for i in range(n+1)]
visited = [-1]*(n+1)
while stack:

    node,depth = stack.pop()
    visited[node] = depth
    
    for i in tree[node]:
        if visited[i] == -1:
            parent[i] = node
            stack.append([i,depth+1])

m = int(input())
for _ in range(m):
    a,b = [int(i) for i in input().split()]

    
    a_d = visited[a]
    b_d = visited[b]
    
    if a_d < b_d:
        
        for _ in range(b_d-a_d):
            b = parent[b]
    else:
        for _ in range(a_d-b_d):
            a = parent[a]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    print(a)
    