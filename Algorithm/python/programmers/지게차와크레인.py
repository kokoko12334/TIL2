def solution(storage, requests):
    
    n = len(storage)
    m = len(storage[0])
    answer = n * m
    all_set = set()
    for i in range(n):
        for j in range(m):
            all_set.add((i, j))
            
    outer = set()
    
    for i in range(n):
        outer.add((i,0))
        outer.add((i, m - 1))
    
    for i in range(m):
        outer.add((0, i))
        outer.add((n - 1, i))
    
    
    # outer에서 추출
    # outer 갱신 
    # 전체에서 제거
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    def cal1(alp):
        nonlocal n, m, outer, all_set
        remove_set = set()
        add_set = set()
        for cor in outer:
            y, x = cor
            if storage[y][x] != alp:
                continue
            
            remove_set.add((y, x))
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                add_set.add((ny, nx))
        print(alp)
        all_set = all_set - remove_set
        outer = (outer | add_set) - remove_set
        print(all_set, len(all_set))
        print(outer, len(outer))
    
    def cal2(alp):
        nonlocal n, m, outer, all_set
        remove_set = set()
        add_set = set()
        
        for cor in all_set:
            y, x = cor
            if storage[y][x] != alp:
                continue
            
            remove_set.add((y, x))
            
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                add_set.add((ny, nx))
        print(alp)
        all_set = all_set - remove_set
        outer = (outer | add_set) - remove_set
        print(all_set, len(all_set))
        print(outer, len(outer))
            
                
            
            
        
        
    for i in range(len(requests)):
        alp = requests[i]
        
        if len(alp) == 1:
            cal1(alp)
        else:
            cal2(alp[0])
        
    
    return answer