def solution(beginning, target):
    n = len(target)
    m = len(target[0])
    arr = [[-1]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if beginning[i][j] == target[i][j]:
                arr[i][j] = 1
    
    # 행 -> 열

    arr2 = [arr[i][:] for i in range(n)]
    answer = float('inf')
    cnt = 0
    for i in range(n):
        flip = False
        for j in range(m):
            if arr2[i][j] == -1:
                flip = True
                cnt += 1
                break
        if flip:
            for j in range(m):
                arr2[i][j] *= -1
            summ = 0
            for k in range(n):
                summ += sum(arr2[k])
            if summ == n*m:
                answer = min(answer, cnt)
    print(answer)
    for i in arr:
        print(i)
    print("##################")
    for i in arr2:
        print(i)
    #열
    for i in range(m):
        flip = False
        for j in range(n):
            if arr2[j][i] == -1:
                flip = True
                cnt += 1
                break
        if flip:
            for j in range(n):
                arr2[j][i] *= -1
            summ = 0
            for k in range(n):
                summ += sum(arr2[k])
            if summ == n*m:
                answer = min(answer, cnt)
    print("#####")
    for i in arr2:
        print(i)
    
    if answer != float('inf'):
        print(answer)
    else:
        answer = -1
    
            
    return answer