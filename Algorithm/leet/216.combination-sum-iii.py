# 음수가 되면 안된다
# rank가 k를 넘어서면 안된다.
from collections import deque
class Solution:
    def combinationSum3(self, k: int, n: int):
        
        queue=deque() 
        queue.append([n,0,[0]])
        answer = []
        
        while queue:
            num,rank,arr = queue.popleft()
            
            for i in range(arr[-1]+1,10):
                
                if num-i > 0 and rank+1 < k:
                    
                    queue.append([num-i,rank+1,arr+[i]])
                elif num-i == 0 and rank+1 == k:
                    answer.append(arr[1:]+[i])
                        
        return answer