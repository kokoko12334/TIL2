import sys

input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

t = [int(i) for i in input().split()]

if len(t) != 1:
    t = set(t[1:])
else:
    t = set()

answer = m
for _ in range(m):
    arr = [int(i) for i in input().split()][1:]
    for p in arr:
        if p in t:
            answer -= 1
            break
print(answer)