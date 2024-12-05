# 시작부터 끝까지 포함
# 시작하자마자 충돌일수 있음.
from collections import defaultdict

def cal(start, end, path):
    sr, sc = start
    er, ec = end
    diff_r = er - sr
    if diff_r < 0:
        for i in range(abs(diff_r)):
            sr -= 1
            path.append((sr, sc))
    elif diff_r > 0:
        for i in range(abs(diff_r)):
            sr += 1
            path.append((sr, sc))
    
    diff_c = ec - sc        
    if diff_c < 0:
        for i in range(abs(diff_c)):
            sc -= 1
            path.append((sr, sc))
    elif diff_c > 0:
        for i in range(abs(diff_c)):
            sc += 1
            path.append((sr, sc))
    


def solution(points, routes):
    robots = []
    for route in routes:
        path = []
        start, end = points[route[0] - 1], points[route[1] - 1]
        path.append((start[0], start[1]))
        for i in range(len(route) - 1):
            start, end = points[route[i] - 1], points[route[i+1] - 1]
            cal(start, end, path)       
        robots.append(path)
        
    maxx = 0
    for i in robots:
        maxx = max(maxx, len(i))
    
    answer = 0
    for t in range(maxx):
        check = defaultdict(int)
        crush = 0
        for i in range(len(routes)):
            if len(robots[i]) <= t:
                continue
            path = robots[i][t]
            if path in check and check[path] == 1:
                crush += 1
            
            check[path] += 1
        
        answer += crush        

    return answer