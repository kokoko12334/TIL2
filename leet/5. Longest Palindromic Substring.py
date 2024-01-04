class Solution:
    def longestPalindrome(self, s: str) -> str:
        



        start = 0
        n = len(s)
        max_value = 1
        answer = ""
        while start < n:

            result = 1
            l = start-1
            r = start+1

            while True:

                if l >= 0:
                    s_l = s[l]
                else:
                    s_l = ""

                if r < n:
                    s_r  = s[r]
                else:
                    s_r = ""

                if s_l == s_r:
                    result += 2
                    l = l-1
                    r = r+1

                else:
                    
                    if max_value <= result:
                        max_value = result
                        answer = s[l+1:r]

                    result -= 1
                    share = (result//2)
                    
                    if share:
                        start = start + share
                    else:
                        start += 1
                    break
        return answer
    







a = Solution()

a.longestPalindrome("cbbd")