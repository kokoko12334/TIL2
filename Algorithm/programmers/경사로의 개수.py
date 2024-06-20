from collections import defaultdict
# https://magentino.tistory.com/299
def solution(grid, d, k):
    answer = 0
    
    d_n = len(d)
    row = len(grid)
    col = len(grid[0])
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    degree_info = defaultdict(set)
    
    for y in range(row):
        for x in range(col):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= col or ny < 0 or ny >= row:
                    continue
                degree = grid[ny][nx] - grid[y][x]
                degree_info[degree].add((y,x, ny, nx))
    result = []
    def back(d_idx, current):
        nonlocal answer
        
        if d_idx == d_n - 1:
            print(result[-1])
            answer += 1
            return
        
        y, x = current
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= col or ny < 0 or ny >= row:
                continue
            
            if (y, x, ny, nx) in degree_info[d[d_idx + 1]]:
                result.append((y,x,ny,nx))
                back(d_idx + 1, (ny, nx))
                result.pop()
    # for k,v in degree_info.items():
    #     print(k,v)

    first_degree = d[0]
    for current in degree_info[first_degree]:
        y,x = current[2], current[3]
        result.append(current)
        back(0, (y,x))
        result.pop()

    
    return answer