class Solution:
    def singleNumber(self, nums) -> int:
        xor=0
        for num in nums:
            xor ^= num
            print(xor)
        return xor
        