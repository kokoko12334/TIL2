import sys
input = sys.stdin.readline
n = int(input())

#t,p
table = {}
for i in range(n):
    t,p = [int(i) for i in input().split()]

    table[i] = [t,p]


dp = [0]*(n+1)


start = n-1
#dp
while start>=0:
    t,p = table[start]
    if start+t > n:
        dp[start] = dp[start+1]

    else:
        if start + t < n:
            if_do = p + dp[start+t]
        else:
            if_do = p
        if_not = dp[start+1]
        dp[start] = max(if_do, if_not)
    start -= 1

# if_not = max(dp[start+1:start+t+1])
print(dp[0])

