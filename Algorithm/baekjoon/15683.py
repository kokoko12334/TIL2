import sys
input = sys.stdin.readline
n, m = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split()])


rotate = {
    (0,1):(1,0),
    (1,0):(0,-1),
    (0,-1):(-1,0),
    (-1, 0):(0,1),
}
g = {
    1: [(0,1)],
    2: [(0,1), (0,-1)],
    3: [(-1, 0), (0,1)],
    4: [(0,-1), (-1,0), (0,1)],
    5: [(1, 0), (0,-1), (-1,0), (0,1),],
}
arr = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] in {1,2,3,4,5}:
            arr.append((i,j,matrix[i][j]))


def dfs(i, arr, matrix):

    y, x, num = arr[i]

    go = g[num]
    case = [go]
    if num in {1, 3, 4}:
        for _ in range(3):
            tmp = []
            for i in go:
                tmp.append(rotate[i])
            case.append(tmp)

    elif num == 2:
        for _ in range(1):
            tmp = []
            for i in go:
                tmp.append(rotate[i])
            case.append(tmp)

    
    for move in case:
        for i in range(len(move)):
            ny = max(move[i][0] * (n-y) + y, 0)
            nx = max(move[i][1] * (m-x) + x, 0)
        
            print(ny,nx)

    return
        

dfs(2, arr, matrix)


# y,x = (2, 2)
# for i in range(len(move5)):
#     ny = max(move5[i][0] * (n-y) + y, 0)
#     nx = max(move5[i][1] * (m-x) + x, 0)
#     print(ny,nx)