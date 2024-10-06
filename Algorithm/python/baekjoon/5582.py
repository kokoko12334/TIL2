
w1, w2 = [input() for _ in range(2)]

dp = [[0]*(len(w1)+1) for _ in range(len(w2)+1)]


answer = 0
for i in range(len(w2)):   #w2
    for j in range(len(w1)):  #w1
        
        if w1[j] == w2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > answer:
                answer = dp[i][j]
        # 만약 최장 공통 부분수열(LCS)이면 띄엄띄엄 연결된 연속된 정보를 담아낸 이 구문도 추가
        # else:
        #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])  

print(answer)


