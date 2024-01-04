class Solution:
    def threeSum(self, nums):
        
        #[[인덱스],진행횟수]
        stack = []
        for i in range(len(nums)):
            lst = [[i],1]
            stack.append(lst)
        
        seen = [[0]*len(nums) for _ in range(len(nums))]
        print(stack)
        answer = []
        while stack:
            indexes, cnt =  stack.pop()
            summ = 0
            for i in indexes:
                summ += nums[i]
            
            for i in range(len(nums)):
                if i in set(indexes):
                    continue
                
                summ += nums[i]
                
                if cnt + 1 <= 2 and seen[indexes[0]][i] == 0:
                    
                    stack.append([indexes + [i], cnt + 1])
                    seen[indexes[0]][i] = 1
                    seen[i][indexes[0]] = 1
                    print(stack)
                elif cnt + 1 == 3:
                    if summ == 0:
                        answer.append(indexes.append(i))


        return answer
    


a = Solution()
a.threeSum(nums = [1,2,3])







seen = [0 for _ in range(3)]*3


a = 1 [0]*3



