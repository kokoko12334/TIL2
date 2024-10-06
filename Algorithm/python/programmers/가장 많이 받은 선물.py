def solution(friends, gifts):
    
    dic = {}
    n = len(friends)
    for i in range(n):
        dic[friends[i]] = i

    arr = [[0]*n for _ in range(n)]


    for g in gifts:
        give, rec = g.split(" ")

        idx_g = dic[give]
        idx_rec = dic[rec]
        arr[idx_g][idx_rec] += 1
    
    g_index = {}

    for f in friends:
        idx = dic[f]
        give = sum(arr[idx])
        given_arr =  [arr[i][idx] for i in range(n)]
        given = sum(given_arr)

        score = give -given        #score가 더 큰사람이 받음
        g_index[idx] = score
    
    result = {k:0 for k in range(n)}
    
    for i in range(n):
        for j in range(i+1,n):

            if arr[i][j] > arr[j][i]:
                result[i] += 1
                
            elif arr[i][j] < arr[j][i]:
                result[j] += 1
                
            else:
                if g_index[i] > g_index[j]:
                    result[i] += 1
                    
                elif g_index[i] < g_index[j]:
                    result[j] += 1

    answer = 0
    for v in result.values():
        answer = max(answer,v)
    

    return answer



solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])