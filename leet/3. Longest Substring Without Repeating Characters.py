
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        size = 0
        seen = {}
        answer = 0
        start = 0
        n = len(s)
        while start < n: 
            
            string = s[start]

            if string not in seen:

                size += 1
                seen[string] = start
                answer = max(answer, size)
                start += 1
            
            else:
                start = seen[string] + 1
                size = 0
                seen = {}
                

        return answer
    
a = Solution()

a.lengthOfLongestSubstring("abcabcbb")



# 다음 문자열이 같지않으면 size를 계속 증가
# 같은 문자열이 포함된다면 그 문자열까지(seen[string]에서의 인덱스)의 최대값이 해당 size라서 더이상 볼 필요없고
# 그다음 문자열을 진행