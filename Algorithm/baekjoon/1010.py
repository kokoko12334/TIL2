import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**7)
t = int(input())

def dp_rec(n,m):

    if n == 0:
        return 0
    
    elif n == 1:
        return n*m
    
    elif n == m:
        return 1
    
    elif dp[n][m] != -1:
        return dp[n][m]

    
    result = 0
    for i in range(1,m-n+2):
        result += dp_rec(n-1,m-i)
    
    dp[n][m] = result
    
    return result
    


for _ in range(t):
    n,m = [int(i) for i in input().split()]
    dp = [[-1]*(m+1) for _ in range(n+1)]
    answer = dp_rec(n,m)
    print(answer)



#comb문제임
t = int(input())

def comb(m,n):
    
    n = min(n, m-n)

    result1 = 1
    for i in range(n):
        result1 *= (m-i)
    result2 = 1
    for i in range(1,n+1):
        result2 *= i

    return result1//result2    
#combination문제임
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    
    answer = comb(m,n)
    print(answer)