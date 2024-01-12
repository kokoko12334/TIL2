class Solution:
    def compress(self, chars) -> int:
        
        n = len(chars)
        l = 0
        r = 0
        answer = ""
        cnt = 0
        while r < n:

            if chars[l] == chars[r]:
                r += 1
                cnt += 1
            else:
                result = ""
                if cnt > 1:
                    result = str(cnt)
                answer += chars[l]+result
                l = r
                cnt = 0
        
        result = ""
        if cnt > 1:
            result = str(cnt)
        answer += chars[l]+result
        
        for i in range(len(answer)):
            chars[i] = answer[i]
        print(chars)
        return len(answer)

a = Solution()


a.compress( chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"])