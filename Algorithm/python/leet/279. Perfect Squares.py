from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        sub = []

        for num in range(1, n+1):
            num_sqrt = num**(1/2)
            if int(num_sqrt) == num_sqrt:
                sub.append(num)

        q = deque()
        dp = dict()
        for num in sub:
            q.append((num,1))
            dp[num] = 1
            if num == n:
                return 1

        while q:
            num, cnt = q.popleft()
            for num2 in sub:
                next_num = num + num2
                if next_num < n and next_num not in dp:
                    q.append((next_num, cnt + 1))
                    dp[next_num] = cnt + 1
                elif next_num == n:
                    dp[next_num] = cnt + 1
                    q = []
                    break

        return dp[n]