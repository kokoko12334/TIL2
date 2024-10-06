from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        seen = set()
        for i in range(n):
            for j in range(i+1, n):
                l = j + 1
                r = n - 1

                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ == target:
                        arr = sorted([nums[i], nums[j], nums[l], nums[r]])
                        string = str(arr)
                        if string not in seen:
                            answer.append([nums[i], nums[j], nums[l], nums[r]])
                            seen.add(string)
                        l += 1
                        r -= 1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1

        # print(answer)

        return answer