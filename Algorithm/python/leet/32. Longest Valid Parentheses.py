class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        arr = [0] * n
        stack = []

        for i in range(n):
            ele = s[i]

            if ele == "(":
                stack.append((ele, i))
            else:
                if stack:
                    idx = stack.pop()[1]
                    arr[idx] = 1
                    arr[i] = 1
        answer = 0
        cnt = 0
        for i in arr:
            if i:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 0
            
        return answer