import sys

input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
g = dict()
arr = [""] * (n + 1)

for i in range(n):
    name = input().strip("\n")
    g[name] = i + 1
    arr[i+1] = name
for _ in range(m):
    p = input().strip("\n")
    if p.isdigit():
        num = int(p)
        print(arr[num])
    else:
        print(g[p])