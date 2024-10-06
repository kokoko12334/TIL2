import sys
input = sys.stdin.readline
n = int(input())
lst = [int(i) for i in input().split()]

inc_dp = [1]*n
dec_dp = [1]*n

inc_max = 1
dec_max = 1
for i in range(1, n):
    if lst[i] >= lst[i-1]:
        inc_dp[i] = inc_dp[i-1] + 1
        if inc_dp[i] > inc_max:
            inc_max = inc_dp[i]
    
for i in range(n-2,-1,-1):
    
    if lst[i] >= lst[i+1]:
        dec_dp[i] = dec_dp[i+1] + 1
        if dec_dp[i] > dec_max:
            dec_max = dec_dp[i]

print(max(inc_max, dec_max))
