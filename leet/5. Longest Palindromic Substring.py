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
    







a = Solution()

print(a.longestPalindrome("cbbd"))