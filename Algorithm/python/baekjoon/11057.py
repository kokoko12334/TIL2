
n = int(input())


if n>=2:
    dp = [[1]*10  for _ in range(n+1)]
    
    for i in range(3,n+1):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][:j+1])
        
    lst = [10,9,8,7,6,5,4,3,2,1]
    
    answer = 0
    for i in range(10):
        answer += (dp[-1][i] *lst[i])
    print(answer%10007)
    
else:
    print(10)

