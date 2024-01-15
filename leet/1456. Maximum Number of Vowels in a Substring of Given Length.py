

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        

        

        vowels = {"a","e","i","o","u"}
        init_v = s[:k]

        cnt = 0
        for i in init_v:
            if i in vowels:
                cnt += 1

        l = 0
        r = k - 1
        n = len(s)
        answer = cnt
        while r < n - 1:
            front = s[l]
            rear = s[r+1]

            if front in vowels:
                cnt -= 1
            if rear in vowels:
                cnt += 1

            l += 1
            r += 1
            answer = max(answer,cnt)
        

        return answer
    


a = Solution()


print(a.maxVowels( s = "abciiidef", k = 3))