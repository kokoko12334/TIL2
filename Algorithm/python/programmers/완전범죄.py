def solution(info, n, m):
    answer = 0
    def knapsack_with_trace(info, m):
        n = len(info)
        max_weight = m - 1
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            val, wt = info[i - 1]
            for w in range(max_weight + 1):
                if wt <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt] + val)
                else:
                    dp[i][w] = dp[i - 1][w]
        
        # 역추적을 통해 선택된 물건의 인덱스를 추적
        selected_items = []
        w = max_weight
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_items.append(i - 1)
                w -= info[i - 1][1]
        
        selected_items.reverse()
        return dp[n][max_weight], selected_items
        
    max_value, items = knapsack_with_trace(info, m)
    
    for i in range(len(info)):
        if i in items:
            continue
        
        n -= info[i][0]
        answer += info[i][0]
        if n <= 0:
            return -1
        
    
    return answer