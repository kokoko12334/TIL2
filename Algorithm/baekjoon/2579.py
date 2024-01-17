
import sys

n = int(sys.stdin.readline())


lst = [0]
for _ in range(n):
    lst.append(int(sys.stdin.readline()))


if n>=2:
    dp = [[0,0]]*(n+1)
    
    ##[1칸, 2칸]
    dp[1] = [lst[1],0]
    dp[2] = [lst[2]+dp[1][0], lst[2]]
    


    for i in range(3, n+1):
        dp[i] = [dp[i-1][1]+lst[i], max(dp[i-2][0],dp[i-2][1]) + lst[i]]
    
    print(max(dp[-1]))

else:
    print(lst[1])
