#[10~0]
from itertools import combinations_with_replacement

def whoWin(c,info):
    rr = [i for i in range(10,-1,-1)]
    info_l = [0]*11
    for cc in c:
        info_l[10-cc] += 1
    p = 0
    l = 0
    for i in range(11):
        
        if info[i] >= info_l[i]:
            if info[i]:
                p += rr[i]
        elif info_l[i] > info[i]:
            
            l += rr[i]
    # print(f"lion:{l}, pech:{p},rr:{c}")
    return l-p,info_l

def solution(n, info):
    c = list(combinations_with_replacement(range(11), n))
    results = []
    mc = 0
    
    for i in c:
        score,res=whoWin(i,info)
        if score > 0 and score >= mc:
            # print(score)
            results.append([score,res])
            mc = score
    results.sort(reverse=True)
    answer=[]
    if results:
        mm = 0
        answer=results[0][1]
        mm = results[0][0]
        for i in range(1,len(results)):
            v,rr = results[i]
            if v == mm:
                for i in range(10,-1,-1):
                    if rr[i] > answer[i]:
                        answer = rr
                        break
                    elif answer[i] > rr[i]:
                        break

    else:
        return [-1]
    
    return answer