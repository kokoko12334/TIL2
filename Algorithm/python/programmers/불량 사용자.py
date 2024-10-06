import sys
sys.setrecursionlimit(10**6)
def solution(user_id, banned_id):
    answer = 0
    arr = []
    for b_id in banned_id:
        arr2 = []
        for u_id in user_id:
            if len(b_id) != len(u_id):
                continue
            flag = True
            
            for i in range(len(b_id)):
                if b_id[i] == "*":
                    continue
                if u_id[i] != b_id[i]:
                    flag = False
                    break
            if flag:
                arr2.append(u_id)
        arr.append(arr2)
    seen = set()
    answer = 0
    
    def dfs(idx, sett):
        nonlocal answer
        # print(idx, sett)
        if idx == len(banned_id):
            lst = list(sett)
            lst.sort()
            key_ = tuple(lst)
            if key_ not in seen:
                answer += 1
                seen.add(key_)
            return
        
        arr2 = arr[idx]
        for i in range(len(arr2)):
            if arr2[i] in sett:
                continue
            sett.add(arr2[i])
            dfs(idx+1, sett)
            sett.remove(arr2[i])
            
    # print(arr)
    dfs(0, set())
    
    return answer