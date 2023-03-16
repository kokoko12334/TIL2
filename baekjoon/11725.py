
n = int(input())

tree = {i:[] for i in range(1,n+1)}

for _ in range(n-1):
    a = [int(i) for i in input().split()]
    tree[a[0]].append(a[1])
    tree[a[1]].append(a[0])


parent = [0]*(n+1)

stack = [1]
seen = {1}

while stack:
    out = stack.pop()
    
    for i in tree[out]:
        if i not in seen:
            parent[i] = out
            stack.append(i)
            seen.add(i)


for i in parent[2:]:
    print(i)

