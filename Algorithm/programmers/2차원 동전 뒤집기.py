def solution(beginning, target):
    #검은색: 0 흰색:1
    answer = 0
    n = len(beginning)
    m = len(beginning[0])
    
    beginning2 = [beginning[i][:] for i in range(n)]
    arr = [0] * m
    for j in range(m):
        if beginning2[0][j] != target[0][j]:
            arr[j] = 1
    
    summ = sum(arr)
    if summ == m:
        for j in range(m):
            beginning2[0][j] = target[0][j]
        answer += 1
            
    elif 0 < summ < m:
        for j in range(m):
            num = arr[j]
            if num:
                for i in range(n): 
                    if beginning2[i][j] == 1:
                        beginning2[i][j] = 0
                    else:
                        beginning2[i][j] = 1
                answer += 1
    for i in range(1, n):
        arr = [0] * m
        for j in range(m):
            if beginning2[i][j] != target[i][j]:
                arr[j] = 1
        summ = sum(arr)
        if summ == m:
            answer += 1  
        elif 0 < summ < m:
            answer = -1
            break
    
    answer2 = 0
    arr = [0] * n
    for i in range(n):
        if beginning[i][0] != target[i][0]:
            arr[i] = 1
    
    summ = sum(arr)
    if summ == m:
        for i in range(n):
            beginning[i][0] = target[i][0]
        answer2 += 1
            
    elif 0 < summ < n:
        for i in range(n):
            num = arr[i]
            if num:
                for j in range(m): 
                    if beginning[i][j] == 1:
                        beginning[i][j] = 0
                    else:
                        beginning[i][j] = 1
                answer2 += 1
        
    for j in range(1, m):
        arr = [0] * n
        for i in range(n):
            if beginning[i][j] != target[i][j]:
                arr[i] = 1
    
        summ = sum(arr)
        if summ == n:
            answer2 += 1
                
        elif 0 < summ < n:
            answer2 = -1
            break
    
    if answer != -1 and answer2 != -1:
        return min(answer, answer2)
    if answer == -1 and answer2 != -1:
        return answer2
    if answer != -1 and answer2 == -1:
        return answer

    return -1