def solution(n, w, num):
    answer = 0
    arr2 = [[0] * w for _ in range(10)]
    
    iteration = n // w
    res = n % w
    number = 1
    for i in range(iteration):
        if i % 2 == 0:
            for j in range(w):
                arr2[i][j] = number
                number += 1
        else:
            for j in range(w-1, -1, -1):
                arr2[i][j] = number
                number += 1
            
    
    if res:
        if iteration % 2 == 0:
            for j in range(res):
                arr2[iteration][j] = number
                number += 1
        else:
            for j in range(w-1, w-res-1, -1):
                arr2[iteration][j] = number
                number += 1
    
    for i in range(10):
        for j in range(w):
            if arr2[i][j] == num:
                y = i
                x = j
                break
    
    # for i in arr2:
    #     print(i)
    # print(y, x)
    if res:
        if arr2[iteration][x]:
            answer = iteration - y + 1
        else:
            answer = iteration - y
    else:
         answer = iteration - y   
    
    return answer