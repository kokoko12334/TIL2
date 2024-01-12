import sys
from bisect import bisect_left

input = sys.stdin.readline



#dp
n = int(input())
boxes = [int(i) for i in input().split()]
boxes = [0] + boxes
dp = [0] * (n+1)

for i in range(n+1):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))







# ###########이분탐색으로
# n = int(input())

# boxes = [int(i) for i in input().split()]

# lis = [boxes[0]]

# for i in range(1,n):
    
#     if lis[-1] < boxes[i]:
#         lis.append(boxes[i])
#     else:
#         idx = bisect_left(lis,boxes[i])
#         lis[idx] = boxes[i]

# print(len(lis))









