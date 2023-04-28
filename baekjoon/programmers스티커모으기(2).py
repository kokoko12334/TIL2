def solution(sticker):
    answer = 0
    n = len(sticker)
    if n>=4:
        dp1 = [0] * (n-1)
        dp1[0] = sticker[0]
        dp1[1] = sticker[1]
        dp1[2] = dp1[0] + sticker[2]
        
        dp2 = [0] * (n-1)
        dp2[0] = 0
        dp2[1] = sticker[1]
        dp2[2] = sticker[2]
        
        
        answer = max(dp2[0],dp2[1],dp2[2],dp1[0],dp1[1],dp1[2])
        for i in range(3,n-1):
            dp1[i] = max(dp1[i-2], dp1[i-3]) + sticker[i]
            dp2[i] = max(dp2[i-2], dp2[i-3]) + sticker[i]
            if dp1[i] > answer:
                answer = dp1[i]
            if dp2[i] > answer:
                answer = dp2[i]
        
        last = max(dp2[-2],dp2[-3]) + sticker[n-1]
        if last> answer:
            answer = last
    else:
        answer = max(sticker)        
    return answer