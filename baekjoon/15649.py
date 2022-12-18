n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            
            s.append(i)
            
            dfs()
            
            s.pop()
            
 
dfs()




# dp = {0:0, 1:1}
# def p(n):
#     if n in dp:
#         return dp[n]
#     else:
#         dp[n] = p(n-1)+p(n-2)    
#         return dp[n]    


# p(100)











