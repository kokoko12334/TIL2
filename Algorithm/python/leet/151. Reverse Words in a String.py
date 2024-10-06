

class Solution:
    def reverseWords(self, s: str) -> str:

        stack = s.split(" ")
        arr = []

        while stack:
            string = stack.pop()
            if string:
                arr.append(string)
        

        answer = arr[0]

        for i in arr[1:]:
            answer += " " + i
        
        return answer
    


a = Solution()

print(a.reverseWords("  hello world  "))