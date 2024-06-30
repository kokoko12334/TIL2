import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = [int(i) for i in input().split()]

lis = [arr[0]]
lis_arr = [0] * n
cnt = 1
lis_arr[0] = 1
for i in range(1, n):
    num = arr[i]
    if num > lis[-1]:
        lis.append(num)
        cnt += 1
        lis_arr[i] = cnt
    else:
        idx = bisect_left(lis, num)

        lis[idx] = num
        lis_arr[i] = idx + 1



lis2 = [arr[-1]]
lis_arr2 = [0] * n
cnt = 1
lis_arr2[0] = 1
for i in range(n-1, -1, -1):
    num = arr[i]
    if num > lis2[-1]:
        lis2.append(num)
        cnt += 1
        lis_arr2[i] = cnt
    else:
        idx = bisect_left(lis2, num)

        lis2[idx] = num
        lis_arr2[i] = idx + 1

answer = 0
for i in range(n):
    answer = max(lis_arr[i] + lis_arr2[i], answer)
print(answer - 1)
