class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        
        nn = len(flowerbed)
        cnt = 0
        for i in range(nn):
            if flowerbed[i] == 0:
                l = i-1
                r = i+1

                if l >= 0 and r < nn:
                    if flowerbed[l] == 0 and flowerbed[r] == 0:
                        cnt += 1
                        flowerbed[i] = 1

                elif l < 0:
                    if r < nn and flowerbed[r] == 0:
                        cnt += 1
                        flowerbed[i] = 1
                    elif r >= nn:
                        cnt += 1
                        flowerbed[i] = 1

                elif r >= nn:
                    if l>=0 and flowerbed[l] == 0:
                        cnt += 1
                        flowerbed[i] = 1
                    elif l < 0:
                        cnt += 1
                        flowerbed[i] = 1
                        
        print(flowerbed)
        answer = False
        if n <= cnt:
            answer = True
        return answer


a = Solution()
a.canPlaceFlowers(flowerbed = [0], n = 1)