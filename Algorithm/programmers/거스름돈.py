def solution(n, money):
    answer = 0
    dp = [-1] * (n+1)
    dp[0] = 1
    coins = set(money)
    def recur(num):
        if dp[num] != -1:
            return dp[num]
        if num == 0:
            return dp[0]
        if num in coins:
            return 1
        
        for m in money:
            m2 = num - m
            if m2 >= 0:
                dp[num] += (recur(m) * recur(m2))
        
        return dp[num]
    recur(n)
    print(dp)
    return answer


a = solution(n=5, money=[1,2,5])