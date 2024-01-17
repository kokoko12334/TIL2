class Solution:
    def convert(self, s: str, numRows: int) -> str:

        answer = ""
        arr = [[] for _ in range(numRows)]
        
        r = 0

        s_rev = s[::-1]
        stack = list(s_rev)

        while stack:

            if r == 0:
                for i in range(numRows):
                    if stack:
                        string = stack.pop()
                        r = i
                        arr[r].append(string)
            else:

                while r>1:
                    r -= 1
                    if stack:
                        string = stack.pop()
                        arr[r].append(string)
                r-=1

        answer = ""
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                answer += arr[i][j]





        return answer
    




a = Solution()
print(a.convert("PAYPALISHIRING",3))




