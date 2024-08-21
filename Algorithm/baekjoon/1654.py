import sys

input = sys.stdin.readline

k, n = [int(i) for i in input().split()]

arr = []
r = 1
for _ in range(k):
    num = int(input())
    r = max(r, num)
    arr.append(num)

arr.sort()
def condition(mid):
    global k, n
    cnt = 0
    for i in range(k):
        cnt += arr[i]//mid
    if cnt >= n:
        return True
    return False
    
l = 1

while l < r:
    mid = (l+r+1)//2

    if condition(mid):
        l = mid
    else:
        r = mid - 1

print(l)