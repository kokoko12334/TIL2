# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess():
    return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        result  = guess(n)
        maxx = 2147483648
        minn = 0
        while result != 0:
            if result == -1:
                maxx = n
                n = n - ((n - minn)//2)
                result = guess(n)
            elif result == 1:
                minn = n
                n = ((maxx-n)//2)+n
                result = guess(n)
        return n