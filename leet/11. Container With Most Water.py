


class Solution:
    def maxArea(self, height) -> int:
        


        l = 0
        r = len(height) - 1 

        answer = 0
        
        while l < r:
            l_v = height[l]
            r_v = height[r]
            h = min(l_v, r_v)
            inter = r - l
            result = h * inter
            answer = max(answer, result)

            if r_v >= l_v:
                l += 1
            else:
                r -= 1



        return answer
    

a = Solution()

print(a.maxArea(height =[1,8,6,2,5,4,8,3,7]))