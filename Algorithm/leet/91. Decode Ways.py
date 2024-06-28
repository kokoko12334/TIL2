class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [[0] * (n+1) for _ in range(n + 1)]

        for i in range(1, n+1):
            num = s[:i]
            int_num = int(num)
            if len(num) == 1 and 1 <= int_num <= 9:
                dp[1][i] = 1
            elif len(num) == 2 and 10 <= int_num <= 26:
                dp[1][i] = 1

        for i in range(2, n+1):
            # print(f"idx:{i-1}, 숫자:{s[i-1]}")
            for j in range(2, i+1):
                # print(f"{j}번의 원소의 수와 가능 수:{dp[j-1][i-1]}")
                num1 = int(s[i-1])
                if 1 <= num1 <= 9:
                    dp[j][i] += dp[j-1][i-1]
            
                num2 = int(s[i-2:i])
                if 10 <= num2 <= 26:
                    # print(f"두번째까지 확인:{int_num}")
                    dp[j][i] += dp[j-1][i-2]
                
        answer = 0
        for i in range(1, n+1):
            answer += dp[i][-1]

        return answer