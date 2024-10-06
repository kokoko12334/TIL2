def solution(a, b, g, s, w, t):
    
    def check(time, a, b, n):
        g_sum = 0
        s_sum = 0
        gs_sum = 0
        for i in range(n):
            current_g = g[i]
            current_s = s[i]
            current_w = w[i]
            current_t = t[i]
            
            cnt = time//(current_t*2)
            if time % (current_t*2) >= current_t:
                cnt += 1
            
            g_sum += min(current_g, cnt * current_w)
            s_sum += min(current_s, cnt * current_w)
            gs_sum += min(current_g + current_s, cnt * current_w)
        
        if a <= g_sum and b <= s_sum and a+b <= gs_sum:
            return True
        return False
    
    l = 0
    r = ((10**9) * 2) * ((10**5) * 2)
    n = len(g)
    while l < r:
        mid = (l+r)//2
        if check(mid, a, b, n):
            r = mid
        else:
            l = mid + 1
        
    return l