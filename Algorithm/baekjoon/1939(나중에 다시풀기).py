
import sys

n, m  = [int(i) for i in sys.stdin.readline().split()]

g = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,c = [int(i) for i in sys.stdin.readline().split()]
    g[a].append([b,c])
    g[b].append([a,c])
f = [int(i) for i in sys.stdin.readline().split()]


s = f[0]
e = f[1]
stack = [[s,9999999999]]
seen = {s}
answer = 0
while stack:
    out = stack.pop()
    land1,weight1 = out[0], out[1]
    print(out)
    for i in g[land1]:
        land2, weight2 = i[0], i[1]
        v = min(weight1, weight2)
        if land2 == e:
            if answer < v:
                answer = v
        else: 
            if land2 not in seen:
                stack.append([land2,v])
                seen.add(land2)


print(answer)