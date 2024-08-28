#0: <-
#1: ->
#2: up
#3: down
#https://prgms.tistory.com/108
from collections import deque, defaultdict
def solution(n, m, x, y, queries):
    answer = 0
    k = len(queries)
    dy = [0,0,-1,1]
    dx = [-1,1,-0,0]
    q = deque([(x,y,k-1)])
    seen = defaultdict(set)
    while q:
        y, x, idx = q.popleft()
        if idx == -1:
            answer += 1
            continue
            
        query = queries[idx]
        d, s = query
        #같은방향
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 > nx or nx >= m or 0 > ny or ny >= n:
            keyy = str(y) + str(x)
            if keyy not in seen[idx-1]:
                q.append((y,x,idx-1))
                seen[idx-1].add(keyy)
        
        #반대방향
        if d in {0, 1}:
            minn = min(s, m)
            if d == 0:    
                for nx in range(x+1, x+minn+1):
                    keyy = str(y) + str(nx)
                    if 0 <= nx and nx < m and keyy not in seen[idx-1]:
                        q.append((y,nx,idx-1))
                        seen[idx-1].add(keyy)
            else:
                for nx in range(x-minn, x):
                    keyy = str(y) + str(nx)
                    if 0 <= nx and nx < m and keyy not in seen[idx-1]:
                        q.append((y,nx,idx-1))
                        seen[idx-1].add(keyy)
        
        else:
            minn = min(s, n)
            if d == 2:
                for ny in range(y+1, y+minn+1):
                    keyy = str(ny) + str(x)
                    
                    if ny >= 0 and ny < n and keyy not in seen[idx-1]:
                        q.append((ny,x,idx-1))
                        seen[idx-1].add(keyy)
            else:
                for ny in range(y-minn, y):
                    keyy = str(ny) + str(x)
                    if ny >= 0 and ny < n and keyy not in seen[idx-1]:
                        q.append((ny,x,idx-1))
                        seen[idx-1].add(keyy)            
            
    return answer