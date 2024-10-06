


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        


        init = sum(nums[:k])

        l = 0
        r = k - 1
        answer = -10001
        answer = max(answer, init/k)
        n = len(nums)
        while r <  n - 1:
            front = nums[l]
            rear = nums[r+1]

            init -= front
            init += rear
            answer = max(answer, init/k)
            l += 1
            r += 1


        return answer
    

a = Solution()

print(a.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))