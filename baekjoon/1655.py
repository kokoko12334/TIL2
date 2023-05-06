from heapq import *
import sys
input = sys.stdin.readline
n = int(input())

max_hq = []
min_hq = []

for i in range(n):
    num = int(input())
    

    if i%2:
        heappush(min_hq, num)
    
    else:
        heappush(max_hq, -num)
        
    if max_hq and min_hq and -max_hq[0] > min_hq[0]:
        a = -heappop(max_hq)
        b = heappop(min_hq)
        heappush(min_hq, a)
        heappush(max_hq, -b)
    print(-max_hq[0])
