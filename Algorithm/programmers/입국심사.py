def solution(n, times):
    def cal(mid):
        cnt = 0
        for t in times:
            cnt += (mid//t)
        return cnt
    l = 0
    r = 1000000000000000001
    
    while l < r:
        mid = (l + r)//2
        if cal(mid) >= n:
            r = mid
        else:
            l = mid + 1
    return l