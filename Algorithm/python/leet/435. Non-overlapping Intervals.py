from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        sorted_arr = sorted(intervals, key = lambda x: x[1])

        e = sorted_arr[0][1]
        answer = 0
        for i in sorted_arr[1:]:
                
            if e > i[0]:    #겹치는 게 있으면 계속 확인하고 그다음 원소에서도 겹치는지, 따라서 end는 기존에 꺼 유지
                answer += 1
            else:
                e = i[1]  #겹치는게 없으면 그다음 진행
    

        return answer
    

a = Solution()

a.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]])