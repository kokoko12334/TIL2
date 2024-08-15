import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
lst = []
hq_max = []
hq_min = []
level_list = defaultdict(int)
for _ in range(n):
    p, l = [int(i) for i in input().split()]
    
    heappush(hq_max,(-l, -p))
    heappush(hq_min,(l, p))
    level_list[p] = l
m = int(input())

for _ in range(m):
    rec = input()
    rec_split = rec.split()

    if rec_split[0] == 'add':
        p, l = int(rec_split[1]), int(rec_split[2])
        heappush(hq_max,(-l, -p))
        heappush(hq_min,(l, p))
        level_list[p] = l

    elif rec_split[0] == 'recommend':
        num = rec_split[1]
        if num == '1':
            l, p = heappop(hq_max)
            p = -p
            l = -l
            while level_list[p] != l:
                l, p = heappop(hq_max)
                p = -p
                l = -l
            print(p)
            heappush(hq_max, (-l, -p))
        elif num == '-1':
            l, p = heappop(hq_min)
            while level_list[p] != l:
                l, p = heappop(hq_min)
            print(p)
            heappush(hq_min, (l, p))

    elif rec_split[0] == 'solved':
        p = int(rec_split[1])
        level_list[p] = 0