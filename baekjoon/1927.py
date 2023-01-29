from heapq import *
import sys


n = int(sys.stdin.readline())

commands = []
for _ in range(n):
    commands.append(int(sys.stdin.readline()))


hq = []

for i  in commands:
    if i == 0:
        if hq:
            print(heappop(hq))
        else:
            print(0)
    else:
        heappush(hq, i)
        