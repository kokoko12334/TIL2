def solution(diffs, times, limit):
        
    def check(level):
        nonlocal limit, n        
        total_time = 0
        pre = 0
        for i in range(n):
            diff = diffs[i]
            time_ = times[i]
            
            add_time = 0 
            if level >= diff:
                add_time = time_
            else:
                add_time = (diff - level) * (pre + time_) + time_
            total_time += add_time
            pre = time_
            if total_time > limit:
                return False
        return True
    
    n = len(diffs)
    answer = 0
    l = 1
    r = 100001
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
            answer = mid
        else:
            l = mid + 1  
    return answer