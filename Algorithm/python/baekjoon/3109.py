import sys

input = sys.stdin.readline

r, c = [int(i) for i in input().split()]

grid = []
for _ in range(r):
    string = input().strip("\n")
    grid.append(list(string))

for i in grid:
    print(i)

seen = set()

stack = []
for i in range(r - 1, -1, -1):
    stack.append((i, 0))
    seen.add((i, 0))
dy = [0, -1, 1]
dx = [1, 1, 1]
answer = 0
while stack:
    y, x = stack.pop()
    print(y, x)    
    if x == c - 1:
        answer += 1
        continue

    for i in range(3):
        ny = dy[i] + y
        nx = dx[i] + x
        if nx < 0 or nx >= c or ny < 0 or ny >= r:
            continue
        print(ny, nx)
        if (ny, nx) in seen or grid[ny][nx] == "x":
            continue

        
        stack.append((ny, nx))
        seen.add((ny, nx))
        
print(answer)