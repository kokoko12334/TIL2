def check(row, beginning, target):
    #검은색: 0 흰색:1
    answer = 0
    n = len(beginning)
    m = len(beginning[0])
    
    beginning2 = [beginning[i][:] for i in range(n)]
    arr = [0] * m
    for j in range(m):
        if beginning2[row][j] != target[row][j]:
            arr[j] = 1
    
    summ = sum(arr)
    if summ == m:
        for j in range(m):
            beginning2[row][j] = target[row][j]
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

    for i in range(n):
        if i == row:
            continue
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
    
    return answer
    
def solution(beginning, target):
    #검은색: 0 흰색:1
    answer = float('inf')
    n = len(beginning)

    for i in range(n):
        result = check(i, beginning, target)
        # print(f"i:{i}, result:{result}")
        if result != -1:
            answer = min(answer, result)
    if answer == float('inf'):
        return -1
    return answer