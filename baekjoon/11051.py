


n, k = [int(i) for i in input().split()]

if n-k < k:
    k = n-k

if k > 0:
    dp1 = [0]*(k)
    dp2 = [0]*(k)


    dp1[0] = n-k+1
    s = n-k+1
    for i in range(1,k):
    
        dp1[i] = dp1[i-1]* (s + 1)
        s += 1


    dp2[0] = k
    s = k
    for i in range(1,k):
        dp2[i] = dp2[i-1] * (s-1)
        s -= 1


    print(dp1[-1]//dp2[-1]%10007)

else:
    print(1)
