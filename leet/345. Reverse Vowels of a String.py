

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        n = len(s)
        l = 0
        r = n-1

        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        s = list(s)
        while l < r:


            if s[l] in vowels and s[r] in vowels:
                s[l],s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowels:
                    l += 1

                if s[r] not in vowels:
                    r -= 1

        answer = ""
        
        for i in s:
            answer += i
        
        return answer
    

a = Solution()
print(a.reverseVowels("leetcode"))