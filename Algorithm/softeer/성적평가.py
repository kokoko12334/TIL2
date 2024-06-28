import sys
from bisect import bisect_right

input = sys.stdin.readline
n = int(input())
arrs = []
for _ in range(3):
    arrs.append([int(i) for i in input().split()])

def cal(arr):
    answer = []
    arr_sorted = sorted(arr)
    dp = dict()
    for num in arr:
        if num in dp:
            answer.append(dp[num])
            continue
            
        idx = bisect_right(arr_sorted, num)
        # print(f"arr:{arr_sorted}, num:{num}, idx:{idx}, n:{n}")
        answer.append(n - idx + 1)
        dp[num] = n - idx + 1
        
    print(*answer)
    
for i in range(3):
    cal(arrs[i])

new_arr = [0] * n
for i in range(n):
    for j in range(3):
        new_arr[i] += arrs[j][i]

cal(new_arr)


