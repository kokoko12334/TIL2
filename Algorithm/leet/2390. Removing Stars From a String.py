

class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for i in s:
            if i != "*":
                stack.append(i)
            else:
                stack.pop()
        answer = ""
        for i in stack:
            answer += i
        return answer
    



a = Solution()

a.removeStars()