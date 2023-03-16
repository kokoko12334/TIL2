import sys

n = int(sys.stdin.readline())

maxx = 0
minn = 101
lst = []

for i in range(n):
    lst_sub = [int(i) for i in sys.stdin.readline().split()]
    for j in lst_sub:
        if maxx < j:
            maxx = j
        if minn > j:
            minn = j
    lst.append(lst_sub)


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def find_zero(seen):
    for i in range(len(seen)):
        for j in range(len(seen[i])):
            if seen[i][j] == 0:
                return [i,j]


answer = [0]

for i in range(0, maxx):
    test = lst
    seen = [[0]*n for _ in range(n)]
    d = 1
    for j in range(n):
        
        for k in range(n):
            if test[j][k] <= i:
                test[j][k] = -1
                seen[j][k] = -1

    first = find_zero(seen)
    if first:
        stack = [first]
        seen[first[0]][first[1]] = 1

        while stack:
            
            out = stack.pop()

            y = out[0]
            x = out[1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny <0 or ny >= n:
                    continue

                if test[ny][nx] != -1 and seen[ny][nx] == 0:
                    stack.append([ny,nx])
                    seen[ny][nx] = 1

            if not stack and find_zero(seen):
                d += 1
                next = find_zero(seen)
                stack.append(next)
                seen[next[0]][next[1]] = 1


    
    answer.append(d)
    
print(max(answer))


