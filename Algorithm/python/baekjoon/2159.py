import sys

input = sys.stdin.readline

n = int(input())

sx, sy = [int(i) for i in input().split()]
dx = [0, 1, 0, -1, 0]
dy = [0, 0, -1, 0, 1]


def cal(m1 ,m2):
    result = 0
    for i in range(2):
        result += abs(m1[i] - m2[i])
    return result

matrix = [[] for _ in range(n)]

for i in range(n):
    x, y = [int(k) for k in input().split()]

    for j in range(5):
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or nx > 100000 or ny < 0 or ny > 100000:
            nx, ny = -1, -1
        matrix[i].append([nx, ny])

INF = float('inf')
dp = [[INF] * n for _ in range(5)]

for i in range(5):
    dp[i][0] = cal(matrix[0][i], [sx, sy])


for i in range(1, n):
    for j in range(5):
        for k in range(5):
            result = dp[k][i-1] + cal(matrix[i-1][k], matrix[i][j])
            if dp[j][i] > result:
                dp[j][i] = result

answer = INF
for i in range(5):
    answer = min(dp[i][-1], answer)
print(answer)