#dp[j][i] = s[:j] 까지의 i번의 원소의 개수를 가지는 경우의 수
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


# 1D 로 푼거 위에서는 이차원으로 각 케이스별로 상세하게 구분해서 했지만 하나씩 가기 보다는 다 더해서 가도 됫었음.
# dp[i] = s[:i+1] 까지의 모든 경우의 수
# 즉 dp[i]는 dp[j][i] 에서 dp[j]에 해당하는 세로열의 값들을 다 합친 것임.
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n+1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1

        for i in range(2, n+1):
            num1 = int(s[i-1])
            if 1 <= num1 <= 9:
                dp[i] += dp[i-1]

            num2 = int(s[i-2:i])
            if 10 <= num2 <= 26:
                dp[i] += dp[i-2]
                
        # print(dp)
        return dp[-1]