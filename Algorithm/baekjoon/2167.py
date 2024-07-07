import sys

input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

arr = []

for _ in range(n):
    arr.append([int(i) for i in input().split()])

pre_fix = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        pre_fix[i][j] = arr[i-1][j-1] + pre_fix[i][j-1] + pre_fix[i-1][j] - pre_fix[i-1][j-1]

k = int(input())

for _ in range(k):
    i, j, x, y = [int(o) for o in input().split()]
    print(pre_fix[x][y] - pre_fix[i - 1][y] - pre_fix[x][j - 1] + pre_fix[i-1][j-1])