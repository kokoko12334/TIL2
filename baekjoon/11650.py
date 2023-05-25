import sys
input = sys.stdin.readline
n = int(input())
lst = [[int(i) for i in input().split()]for _ in range(n)]
lst.sort(key = lambda x: (x[0],x[1]))
for i in lst:
    print(*i)