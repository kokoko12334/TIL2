
n = int(input())
lst = [0]

for j in [int(i) for i in input().split()]:
    lst.append(j)

dp = [0]*(n+1)

dp[1] = lst[1]

for i in range(2, n+1):
    maxx = lst[i]    # 초기값 원래 값 그자체
    iteration = (i//2)
    
    for j in range(1, iteration+1):
        a = dp[i-j] +dp[j]
        if a > maxx:
            maxx = a
    dp[i] = maxx
        
print(dp[-1])
