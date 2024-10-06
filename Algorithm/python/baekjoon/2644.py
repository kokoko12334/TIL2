import sys
input = sys.stdin.readline

n = int(input())
num1, num2 = [int(i) for i in input().split()]

m = int(input())
g = {i:[] for i in range(1,n+1)}

for _ in range(m):
    p,c = [int(i) for i in input().split()]
    g[p].append(c)
    g[c].append(p)

answer = -1
stack = [[num1,0]]
seen = {num1}
while stack:
    out = stack.pop()
    num, d = out[0], out[1]
    for i in g[num]:
        if i == num2:
            answer = d + 1
            stack = []
            break
        if i not in seen:
            stack.append([i,d+1])
            seen.add(i)

print(answer)