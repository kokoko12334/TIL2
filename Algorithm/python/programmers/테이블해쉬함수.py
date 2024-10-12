def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : (x[col-1], -x[0]))
    arr = []
    for i in range(row_begin-1, row_end):
        arr.append(sum([num%(i+1) for num in data[i]]))
    
    answer = 0
    for num in arr:
        answer ^= num
    return answer