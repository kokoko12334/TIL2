class Solution:

    def cal(self, piles, num):
        
        cnt = 0
        for i in piles:
            
            hour = i//num
            
            if i%num:
                hour += 1
            
            cnt += hour
        return cnt

    def minEatingSpeed(self, piles, h: int) -> int:
        piles.sort()
    
        l = 1
        r = piles[-1]
        mid = ((r-l)//2) + l
        result = self.cal(piles,mid)

        while l < r:
        
            if result > h:
                l = mid + 1
                mid = l + ((r-l)//2)
            
            elif result <= h:
                r = mid - 1
                mid = r - ((r-l)//2)

            result = self.cal(piles,mid)
            
        if result > h:
            mid += 1
            
        return mid