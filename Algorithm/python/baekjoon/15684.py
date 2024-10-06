from itertools import combinations
import sys
sys.setrecursionlimit(10**6)

# n = 가로 h 세로
n,m,h = [int(i) for i in sys.stdin.readline().split()]
ladder = [[0]*(n+1) for _ in range(h+1)]

lst = [list(range(n+1))]
for _ in range(h):
    lst.append([0]*(n+1))
for _ in range(m):
    y,x = [int(i) for i in sys.stdin.readline().split()]
    ladder[y][x] = 1
    ladder[y][x+1] = -1


def dfs(y,x):
    if y == h + 1:
        return
    lst2[y][x] = lst2[y-1][x] + ladder[y][lst2[y-1][x]]
    
    dfs(y+1,x)

def put(lst,n):
    global flag
    if n == 1:
        y,x = lst[0][0], lst[0][1]
        ladder[y][x] += 1
        ladder[y][x+1] -= 1
        return 1
    elif n == 2:
        y1,x1,y2,x2 = lst[0][0], lst[0][1], lst[1][0], lst[1][1]
        if y1 == y2 and abs(x1-x2) == 1:
            flag = False
            return 0
        else:
            ladder[y1][x1] += 1
            ladder[y1][x1+1] -= 1
            ladder[y2][x2] += 1
            ladder[y2][x2+1] -= 1 
            return 1
    else:
        y1,x1,y2,x2,y3,x3 = lst[0][0], lst[0][1], lst[1][0], lst[1][1],lst[2][0], lst[2][1]
        if (y1 == y2 and abs(x1-x2) == 1) or (y1 == y3 and abs(x1-x3) == 1) or (y2 == y3 and abs(x2-x3) == 1):
            flag = False
            return 0 
        else:
            ladder[y1][x1] += 1
            ladder[y1][x1+1] -= 1
            ladder[y2][x2] += 1
            ladder[y2][x2+1] -= 1
            ladder[y3][x3] += 1
            ladder[y3][x3 +1] -= 1
            return 1

def disput(lst, n):
 
    if n == 1:
        y,x = lst[0][0], lst[0][1]
        ladder[y][x] -= 1
        ladder[y][x+1] += 1
    elif n == 2:
        y1, x1, y2, x2 = lst[0][0], lst[0][1], lst[1][0], lst[1][1]
        
        ladder[y1][x1] -= 1
        ladder[y1][x1+1] += 1
        ladder[y2][x2] -= 1
        ladder[y2][x2+1] += 1
    else:
        y1, x1, y2, x2, y3, x3 = lst[0][0], lst[0][1], lst[1][0], lst[1][1], lst[2][0], lst[2][1]
        
        ladder[y1][x1] -= 1
        ladder[y1][x1+1] += 1
        ladder[y2][x2] -= 1
        ladder[y2][x2+1] += 1
        ladder[y3][x3] -= 1
        ladder[y3][x3 + 1] += 1

c = []
for i in range(1,h+1):
    for j in range(1,n+1):
        if j == n:
            continue
        else:
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                c.append([i,j])

flag = True
lst2 = [l[:] for l in lst]

for i in range(1,n+1):
    dfs(1,i)
    if lst2[h][i] != i:
        flag = False
        break

if flag:
    answer = 0

else:
    answer = -1
    flag2 = True
    for num in [1,2,3]:
        if flag2:
            cases = list(combinations(c,num))
            for i in cases:
                flag = True
                if put(i,num):
                    lst2 = [l[:] for l in lst]
                    for j in range(1,n+1):
                        dfs(1,j)
                        if lst2[h][j] != j:
                            flag = False
                            break
                    disput(i,num)
                if flag:
                    
                    answer = num
                    flag2 = False
                    break

print(answer)






