import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

r, c =  [int(i) for i in input().split()]

matrix = []

for _ in range(r):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

dy = [0, 1, 0, -1] # R, D, L, U
dx = [1, 0, -1, 0]
direction = ["R", "D", "L", "U"]
seen = [[0] * c for _ in range(r)]
answer = []
arr = []
max_happy = 0
def dfs(y, x, cnt, happy):
    global answer, max_happy
    if (y, x) == (r-1, c-1):
        if max_happy < happy:
            answer = arr[:]
            max_happy = happy
        return
    
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if nx < 0 or nx >= c or ny < 0 or ny >= r:
            continue
        
        if seen[ny][nx]:
            continue
        
        arr.append(direction[i])
        seen[ny][nx] = 1
        dfs(ny, nx, cnt+1, happy + matrix[ny][nx])
        arr.pop()
        seen[ny][nx] = 0

seen[0][0] = 1
dfs(0, 0, 1, matrix[0][0])

print("".join(answer))