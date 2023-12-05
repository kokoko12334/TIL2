


def search(lst,i,j):
    v = lst[i][j]
    y,x = i,j
    di = [0,0,0,0]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    idx = -1
    for i in range(4):
        idx += 1
        ny = dy[i] + y
        nx = dx[i] + x
        if nx < 0 or nx>= m or ny <0 or ny >= n:
            continue
        while (0<=ny and ny<n) and (0<=nx and nx<m) :
            if lst[ny][nx] == 6:
                break
            if lst[ny][nx] == 0:
                di[idx] += 1
            if ny > y:
                ny += 1
            elif ny < y:
                ny -= 1
            elif nx > x:
                nx += 1
            elif nx < x:
                nx -= 1
    return di


n,m = [int(i) for i in input().split()]

lst = [[int(i) for i in input().split()]for _ in range(n)]



for i in lst:
    print(i)

total = n*m
stack = []
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            total -= 1
            if lst != 6:
                stack.append([i,j])


maxx = float("int")

##최소값







