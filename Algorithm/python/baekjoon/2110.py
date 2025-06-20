import sys

input = sys.stdin.readline

N, M = [int(i) for i in input().split()]

home = []
for _ in range(N):
    home.append(int(input()))
home.sort()

def check(mid):
    global N, M
    
    cnt = 1
    now = home[0]
    for i in range(1, N):
        diff = home[i] - now
        
        if diff < mid:
            continue
        
        if diff >= mid:
            now = home[i]
            cnt += 1 
    
    return cnt >= M

l = 0
r = 1000000001

answer = 0
while l < r:
    mid = (l + r) // 2
    
    if check(mid):
        l = mid + 1
        answer = max(mid, answer)
    else:
        r = mid

print(answer)
