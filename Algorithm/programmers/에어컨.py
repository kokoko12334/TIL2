def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    INF = float('inf')
    n = len(onboard)
    
    t1 += 10
    t2 += 10
    temperature += 10
    
    dp = [[INF]*n for _ in range(51)]
    
    dp[temperature][0] = 0
    if 0 <= temperature+1 <= 50:
        dp[temperature+1][0] = a
    if 0 <= temperature-1 <= 50:
        dp[temperature-1][0] = a
    
    for j in range(1, n):
        for i in range(51):

            if onboard[j] and (i < t1 or i > t2):
                continue

            v1,v2,v3 = INF, INF, INF
            
            if 0 <= i - 1 <= 50: 
                if i - 1 < temperature:
                    v1 = dp[i-1][j-1]
                else:
                    v1 = dp[i-1][j-1] + a
            
            if i == temperature:
                v2 = dp[i][j-1]
            else:
                v2 = dp[i][j-1] + b
            
            if 0 <= i + 1 <= 50:
                if i+1 <= temperature:
                    v3 = dp[i+1][j-1] + a
                else:
                    v3 = dp[i+1][j-1]
                
            dp[i][j] = min(v1, v2, v3)
    
    answer = INF
    if onboard[-1]:
        for i in range(t1,t2+1):
            answer = min(answer, dp[i][-1])
            # print(f"온도:{i} {dp[i][-1]}")
    else:
        for i in range(51):
            answer = min(answer, dp[i][-1])
            # print(f"온도:{i} {dp[i][-1]}")
            
    return answer