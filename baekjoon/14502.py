from collections import deque
import copy
import sys

sys.setrecursionlimit(10**5)

n,m = [int(i) for i in sys.stdin.readline().split()]
lst = [sys.stdin.readline().split() for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


que = deque()
seen = set()
zero = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == '2':
            a = str(i)+'.'+str(j)
            que.append(a)
            seen.add(a)
        elif lst[i][j] == '0':
            a = str(i)+'.'+str(j)
            zero.append(a)

def bfs():       
    if que2:
        out = que2.popleft()
        y, x = [int(i) for i in out.split('.')]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny <0 or ny >= n:
                continue

            a = str(ny)+'.'+str(nx)
            if test[ny][nx] == '0' and a not in seen:
                test[ny][nx] = '2'
                que2.append(a)
                seen2.add(a)
        bfs()


answer = 0
for i in range(len(zero)):
    next = zero[:i]+zero[i+1:]
    for j in range(len(next)):
        next2 = next[:j]+next[j+1:]
        for k in range(len(next2)):
            test = copy.deepcopy(lst)
            que2 = copy.deepcopy(que)
            seen2 = copy.deepcopy(seen)
            y,x = [int(i) for i in zero[i].split('.')]
            test[y][x] = '1'
            y,x = [int(i) for i in next[j].split('.')]
            test[y][x] = '1'
            y,x = [int(i) for i in next2[k].split('.')]
            test[y][x] = '1'

            bfs()
            num = 0
            for k in test:
                num += k.count('0')    
            if num >answer:
                answer = num


print(answer)




####################################################################
########좀더 경량화 버전 pypy3로 제출해야 통과됨######################
#참고로 pypy3는 속도를 빠르지만 여러 문자열처리나 재귀처리에서 pyhon3보다 밑임.
#위 코드와 차이점은 deepcopy를 쓰지 않았고 방문처리를 하지 않았음.

n, m = [int(i) for i in sys.stdin.readline().split()]
lst = [sys.stdin.readline().split() for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 얘는 안쓸거라서 deque안쓰고 그냥 리스트
que = []
zero = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == '2':
            
            que.append([i,j])
            
        elif lst[i][j] == '0':
            
            zero.append([i,j])

def bfs():
    if que2:
        out = que2.popleft()
        y, x = [i for i in out]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if test[ny][nx] == '0':
                test[ny][nx] = '2'
                que2.append([ny,nx])
                
        bfs()


answer = 0
for i in range(len(zero)):
    next = zero[:i]+zero[i+1:]
    for j in range(len(next)):
        next2 = next[:j]+next[j+1:]
        for k in range(len(next2)):
            test = [i[:] for i in lst]   #deepcoy대신에 이런식으로 하는 것이 좋음.
            que2 = deque()
            for q in que:
                que2.append(q)
            
            y, x = [p for p in zero[i]]
            test[y][x] = '1'
            y, x = [p for p in next[j]]
            test[y][x] = '1'
            y, x = [p for p in next2[k]]
            test[y][x] = '1'

            bfs()
            num = 0
            for k in test:
                num += k.count('0')
            if num > answer:
                answer = num


print(answer)