import sys
input = sys.stdin.readline
n = int(input())
lst = [[int(i) for i in input().split()]for _ in range(n)]
g = {i:[] for i in range(n)}

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            g[i].append(j)

answer = [[0]*n for _ in range(n)]

stack = []

for i in range(n):
    for j in range(n):
        
        seen = [True]*n
        stack.append(i)

        while stack:
            out = stack.pop()
            for k in g[out]:
                if k == j:
                    answer[i][j] = 1
                    stack = []
                    break
                if seen[k]:
                    stack.append(k)
                    seen[k] = False

for i in answer:
    print(*i)