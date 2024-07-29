def solution(n, cores):
    
    core_n = len(cores)
    if core_n >= n:
        return n

    tasks = n - core_n  
    l = 0  
    r = max(cores) * n 
    # print(f"남은 작업량:{tasks}")
    while l < r:
        mid = (l + r) // 2
        result = sum(mid // core for core in cores)
        # print(f"{mid}시간:{result}작업량, l,r{l, r}")
        if result >= tasks:
            r = mid
        else:
            l = mid + 1 
            
    h = l
    # print(f"h:{h}")
    pre_h = h - 1
    result = sum(pre_h // core for core in cores)
    tasks -= result  

    answer = 0
    for i in range(core_n):
        if h % cores[i] == 0:  
            tasks -= 1
        
        if tasks == 0:  
            answer = i + 1 
            break
            
    return answer