def cal(q,matrix):

    r_dif = q[2] - q[0] #세로
    c_dif = q[3] - q[1] #가로
    
    s_r = q[0] - 1
    s_c = q[1] - 1
    
    s_val = matrix[s_r][s_c]
    
    min_val = s_val
    arr = [s_val]
    arr_idx = {0:[s_r,s_c]}
    idx = 1
    #->
    for _ in range(1,c_dif+1):   
        s_c += 1
        
        arr.append(matrix[s_r][s_c])
        min_val = min(matrix[s_r][s_c],min_val)
        arr_idx[idx] = [s_r,s_c]
        idx += 1
    #아래 
    for _ in range(1,r_dif+1):
        s_r += 1

        arr.append(matrix[s_r][s_c])
        min_val = min(matrix[s_r][s_c],min_val)
        arr_idx[idx] = [s_r,s_c]
        idx += 1
    # <-
    for _ in range(1,c_dif+1):
        s_c -= 1

        arr.append(matrix[s_r][s_c])
        min_val = min(matrix[s_r][s_c],min_val)
        arr_idx[idx] = [s_r,s_c]
        idx += 1
    # 위로
    for _ in range(1,r_dif):
        s_r -= 1

        arr.append(matrix[s_r][s_c])
        min_val = min(matrix[s_r][s_c],min_val)
        arr_idx[idx] = [s_r,s_c]
        idx += 1
    #맨끝에 것만 앞으로
    arr2 = [arr[-1]] + arr[:-1]

    for k,v in arr_idx.items():
        y=v[0]
        x=v[1]
        matrix[y][x] = arr2[k] 
    
    
    
    return min_val, matrix 


def solution(rows, columns, queries):
    
    matrix = [[0]*columns for _ in range(rows)]
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            matrix[i-1][j-1] = (i-1)*columns + j
            
    answer = []
    for q in queries:
        min_val, matrix = cal(q,matrix)
        answer.append(min_val)
        
    
    return answer