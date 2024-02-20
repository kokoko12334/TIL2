from itertools import combinations
def check(relation, answer, remove_rows, rows):
    sett = set()
    n = len(relation)
    
    for i in range(n):
        n_str = ""
        
        for j in rows:
            n_str += relation[i][j]
        print(n_str)
        if n_str not in sett:
            sett.add(n_str)
        else:
            return answer, remove_rows
    
    answer += 1
    for i in rows:
        remove_rows.add(i)
    print(f"제거해야할거:{remove_rows}")
    return answer, remove_rows


def solution(relation):
    c = len(relation)
    r = len(relation[0])
    idx = {i for i in range(r)}
    answer = 0
    # for cnt in range(2,r+1): #1,2,3,4..
    for cnt in range(1,r+1): #1,2,3,4..
        
        comb = list(combinations(idx,cnt))
        remove_sub = set()
        for rows in comb: # 각 row들
            print(rows)
            answer,remove_rows = check(relation,answer,remove_sub,rows)
        idx = idx - remove_rows
        
    
    return answer