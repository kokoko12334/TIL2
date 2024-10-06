from heapq import *
import sys
input = sys.stdin.readline
n = int(input())

lst = [[int(i) for i in input().split()]for _ in range(n)]

lst.sort(key = lambda x: x[0])

hq = []
heappush(hq, lst[0][1])

for i in range(1,n):
    if lst[i][0] < hq[0]:
        heappush(hq, lst[i][1])
    else:
        heappop(hq)
        heappush(hq, lst[i][1])

print(len(hq))



