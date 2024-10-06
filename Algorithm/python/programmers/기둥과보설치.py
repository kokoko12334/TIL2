# 0:기둥, 1:보 
# 0: 삭제, 1: 설치 보는 오른쪽(좌표기준), 기둥은 위쪽
def solution(n, build_frame):
    
    matrix = [ [[0,0] for _ in range(n+1)] for _ in range(n+1)]
    answer = set()
    for command in build_frame:
        x, y, a, b = command
        if a == 0 and b == 1: # 기둥설치
            if y != 0 and matrix[y][x][0] == 0 and matrix[y][x][1] == 0:
                continue
            matrix[y][x][0] += 1
            matrix[y+1][x][0] += 1
            answer.add((x,y,0))
            
        elif a == 0 and b == 0: #기둥 제거
            if y+2 <= n and matrix[y+2][x][0] >= 1:
                continue
            if matrix[y+1][x][1] >= 1:
                if 0 <= x-1 and matrix[y+1][x-1][1] == 0 and matrix[y+1][x-1][0] == 0:
                    continue
                if x+1 <= n and matrix[y+1][x+1][1] == 0 and matrix[y+1][x+1][0] == 0:
                    continue
            matrix[y][x][0] -= 1
            matrix[y+1][x][0] -= 1
            answer.remove((x,y,0))
            
        elif a == 1 and b == 1: #보 설치
            if matrix[y][x][0] == 0:
                left = 0
                right = 0
                if 0 <= x-1 and matrix[y][x-1][1] >= 1:
                    left = 1
                if x+1 <= n and matrix[y][x+1][1] >= 1:
                    right = 1
                if left == 0 or left == 0:
                    continue
            matrix[y][x][1] += 1
            matrix[y][x+1][1] += 1
            answer.add((x,y,1))
            
        elif a == 1 and b == 0: # 보 제거
            left = 0
            right = 0
            if 0 <= x-1 and matrix[y][x-1][1] >= 1 and matrix[y][x-1][0] == 0:
                left = 1
            if x+1 <= n and matrix[y][x+1][1] >= 1 and matrix[y][x+1][0] == 0:
                right = 1
            if left == 1 or right == 1:
                continue
            matrix[y][x][1] -= 1
            matrix[y][x+1][1] -= 1
            answer.remove((x,y,1))
            
    answer = [list(i) for i in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    
    return answer