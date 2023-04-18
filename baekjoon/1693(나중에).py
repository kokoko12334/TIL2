

n = int(input())
g = {i:[] for i in range(1,n+1)}
for _ in range(n-1):
    a,b = [int(i) for i in input().split()]
    g[a].append(b)
    g[b].append(a)


print(g)


