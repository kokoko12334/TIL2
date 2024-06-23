from collections import defaultdict
class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = defaultdict(int)

        def dfs(arr):
            # print("######")
            str_ele = ""
            n = len(arr)
            for i in range(n):
                str_ele += str(arr[i])
            # print(f"n: {n},str:{str_ele}, dp: {dp[str_ele]}")
            if dp[str_ele]:
                return dp[str_ele]
            
            if n == 1 or n == 0:
                return 1

            if n == 2:
                return 2

            result = 0
            for i in range(n):
                re1 = dfs(arr[i+1:])
                re2 = dfs(arr[:i])
                result += (re1 * re2)
            # print(f"{str_ele}의 결과:{result}")
            dp[str_ele] = result
            return result
        
        arr = [i for i in range(1, n+1)]
        answer = dfs(arr)
        # print(dp)
        return answer