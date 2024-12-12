from collections import deque
from itertools import combinations
n , m = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split()])


clear = n * n
virus = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            matrix[i][j] = -2
            virus.append((i, j, 0))
            clear -= 1
        elif matrix[i][j] == 1:
            matrix[i][j] = -1
            clear -= 1


if not clear:
    print(0)
else:


    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    def bfs(q, matrix):
        global clear
        start = set()
        for node in q:
            y, x = node[0], node[1]
            start.add((y, x))
        # print(start)
        result = 0
        infected = 0
        while q:
            y, x, cnt = q.popleft()
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if not matrix[ny][nx]:
                    matrix[ny][nx] = cnt + 1
                    q.append((ny, nx, cnt + 1))
                    infected += 1
                    result = max(result, cnt + 1)

                if matrix[ny][nx] == -2 and (ny, nx) not in start:
                    q.append((ny, nx, cnt + 1))
                    start.add((ny, nx))

        # print("##############")
        # for i in matrix:
        #     print(i)           
        if infected != clear:
            return 999999999

        return result

    lst = list(combinations(virus, m))
    answer = 999999999
    for cases in lst:
        q = deque()
        for c in cases:
            q.append(c)
        matrix_copy = [matrix[i][:] for i in range(n)]
        result = bfs(q, matrix_copy)
        answer = min(result, answer)

    if answer == 999999999:
        print(-1)
    else:
        print(answer)