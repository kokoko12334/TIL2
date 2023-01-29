import sys
from heapq import *

n = int(sys.stdin.readline())
commands = [int(sys.stdin.readline()) for _ in range(n)]


hq = []

for i in commands:
    if i == 0:
        if hq:
            
            print(heappop(hq)[1])    
        else:
            print(0)
    else:
        heappush(hq, (abs(i),i))            