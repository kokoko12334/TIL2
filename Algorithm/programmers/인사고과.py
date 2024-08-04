def solution(scores):
    answer = 0
    
    n = len(scores)
    arr = [(scores[i][0], scores[i][1], i)for i in range(n)]
    sorted_arr = sorted(arr, key = lambda x: (-x[0], x[1]))
    
    maxx = sorted_arr[0][1]
    no = set()
    for i in range(1, n):
        
        if maxx > sorted_arr[i][1]:
            no.add(sorted_arr[i][2])
        else:
            maxx = max(maxx, sorted_arr[i][1])

    new_arr = []
    for i in range(n):
        if i not in no:
            new_arr.append((scores[i][0]+scores[i][1],i))
    new_arr = sorted(new_arr, key=lambda x: -x[0])
    
    answer = -1
    
    for i in range(len(new_arr)):
        idx = new_arr[i][1]
        if idx == 0:
            answer = i + 1 
    return answer