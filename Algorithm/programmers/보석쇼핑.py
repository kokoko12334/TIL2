from collections import defaultdict
def solution(gems):
    n = len(gems)
    g = defaultdict(int)
    tar = len(set(gems))
    r = 0
    l = 0
    cnt = 1
    g[gems[0]] = 1
    #["a", "b", "b", "c", "c", "a", "b", "c", "b"]
    answer = float('inf')
    result = [1,1]
    while l <= r:
        
        if cnt != tar:
            if r < n-1:
                r += 1
                gem = gems[r]
                if not g[gem]:
                    cnt += 1
                g[gem] += 1
            else:
                break
            
        else:
            if answer > r-l:
                result = [l,r]
                answer = r-l
            gem = gems[l]
            g[gem] -= 1
            l += 1
            if not g[gem]:
                cnt -= 1
 
    if answer == float("inf"):
        return [1,n]
    
    return [result[0]+1, result[1]+1]