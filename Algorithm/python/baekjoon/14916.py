

n  = int(input())

dp = [0,-1,1,-1,2,1]

if n>= 5:
    re = n%5
    a = n//5
    if re%2 == 0:
        answer = a + (re//2)

    else:

        while True:
            re += 5
            a -= 1
            if re%2 == 0:
                answer = a + (re//2)
                break
    print(answer)
else:
    print(dp[n])


