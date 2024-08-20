def solution(targets):
    n = len(targets)
    answer = 1
    t1 = sorted(targets, key=lambda x :(x[0], x[1]))
    l = 0
    r = 1
    most_end = t1[l][1]
    
    while r < n:
        if most_end > t1[r][0]:
            most_end = min(t1[r][1], most_end)
            r += 1
        else:
            l = r
            most_end = t1[l][1]
            r += 1
            answer += 1
        
    return answer