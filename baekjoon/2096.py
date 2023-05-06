import sys
input = sys.stdin.readline
n = int(input())


lst = [int(i) for i in input().split()]
dp_max = lst[:]
dp_min = lst[:]

for _ in range(1,n):
    lst = [int(i) for i in input().split()]
    next = [0,0,0]
    next2 = [0,0,0]

    next[0] = max(dp_max[:2]) + lst[0]
    next[1] = max(dp_max[:]) + lst[1]
    next[2] = max(dp_max[1:]) + lst[2]
    dp_max = next 

    next2[0] = min(dp_min[:2]) + lst[0]
    next2[1] = min(dp_min[:]) + lst[1]
    next2[2] = min(dp_min[1:]) + lst[2]
    dp_min = next2
    
print(max(dp_max), min(dp_min))

