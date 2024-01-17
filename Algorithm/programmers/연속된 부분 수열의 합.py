
from heapq import heappush, heappop
def solution(sequence, k):
    answer = []


    l = 0
    r = 0
    n = len(sequence)
    answers = []
    init = True
    
    while r < n:
        if init:            
            sub_seq = sequence[l:r+1]
            result = sum(sub_seq)
            init = False

        if result > k:
            if l < r:
                result -= sequence[l]
                l += 1
            else:
                l += 1
                r += 1
                init = True

        elif result == k:
            heappush(answers,[r-l, [l,r]])
            
            if l < r:
                result -= sequence[l]
                l += 1
            else:
                l += 1
                r += 1
                init = True
        else:
            r += 1
            if r < n:
                result += sequence[r]
    
    print(answers)
    answer = heappop(answers)[1]
    
    return answer


print(solution([1, 1, 1, 2, 3, 4, 5],5))








