from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        n = len(temperatures)
        stack = [[temperatures[0],0]]
        
        answer = [0]*n
        for i in range(1,n):

            v2 = temperatures[i]
            
            while stack and v2 > stack[-1][0]:
                _,idx = stack.pop()
                answer[idx] = i - idx

            stack.append([v2,i])

        return answer
            

a = Solution()
a.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])