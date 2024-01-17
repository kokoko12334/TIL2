
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        n = len(s)
        digit = ""
        for i in range(n):

            
            if str.isdigit(s[i]):
                digit += s[i]
                continue    

            elif s[i] != "]":
                if digit:
                    stack.append(digit)
                    digit = ""
                stack.append(s[i])

            else:
                result = ""
                while True:
                    string = stack.pop()
                    result += string
                    if string == "[":
                        result = result[:-1]
                        result = result[::-1]
                        break            
                
                repeat = int(stack.pop())

                result2 = result * repeat

                for j in result2:
                    stack.append(j)
        
        answer = ""
        for i in stack:
            answer += i

        return answer
    

a = Solution()

print(a.decodeString("100[leetcode]"))


