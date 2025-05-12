import sys

input = sys.stdin.readline

N, M = [int(i) for i in input().split()]

arr = [int(i) for i in input().split()]


prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i-1]


for _ in range(M):
    a, b = [int(i) for i in input().split()]
    print(prefix_sum[b] - prefix_sum[a-1])    
        

