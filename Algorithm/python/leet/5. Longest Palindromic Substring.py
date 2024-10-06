# dp[i][j] = if dp[i+1][j-1] == 1 and s[i] == s[j] => 1 else 0
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        answer = (0,0)
        for i in range(n):
            dp[i][i] = 1
            if i+1 < n:
                if s[i] == s[i+1]:
                    dp[i][i+1] = 1
                    if answer[1] - answer[0] < i+1 - i:
                        answer = (i,i+1)
        
        for dif in range(2,n):
            for i in range(n):
                j = dif + i
                if j < n:
                    if dp[i+1][j-1] and s[i] == s[j]:
                        dp[i][j] = 1
                        if answer[1] - answer[0] < j - i:
                            answer = (i,j)                
                        
                    # print(f"from:{i}, to:{j}, str:{s[i:j+1]}, len:{dp[i][j]}")
        # for i in dp:
        #     print(i)

        return s[answer[0]:answer[1]+1]

# 투포인터
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        answer = ""
        max_v = 0
        #odd
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                res = r - l + 1
                if res >= max_v:
                    max_v = res
                    answer = s[l:r+1]  
                l -= 1
                r += 1
        #even
        for i in range(n):
            l = i
            r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                res = r - l + 1
                if res >= max_v:
                    max_v = res
                    answer = s[l:r+1]  
                l -= 1
                r += 1


        return answer
    
