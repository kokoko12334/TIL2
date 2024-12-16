# 거리가 같다면 행번호작은거, 열번호 작은거
# 소모한 거리 * 2만큼 충전
#연료 없으면 break
# 단 목적지에 가서 연료 0인경우는 실패가 아님
from collections import deque
n, m, oil = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    arr = [int(i) for i in input().split()]
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1 # 길
        else:
            arr[i] = -2 # 벽
    matrix.append(arr)

taxi_y, taxi_x = [int(i) - 1 for i in input().split()]
customers = []
for _ in range(m):
    sy, sx, dy, dx = [int(i) - 1 for i in input().split()]
    info = (sy, sx, dy, dx)
    customers.append(info)

mapping = dict()
for i in range(m):
    sy, sx, dy, dx = customers[i]
    mapping[(sy, sx)] = (dy, dx)

ddy = [0, 1, 0, -1]
ddx = [1, 0, -1, 0]
def bfs(sy, sx):
    global n

    q = deque([(sy, sx, 0)])
    matrix_copy[sy][sx] = 0
    arr = []
    while q:
        sy, sx, dis = q.popleft()
        if (sy, sx) in mapping.keys():
                arr.append((dis, sy, sx))

        for i in range(4):
            ny = ddy[i] + sy
            nx = ddx[i] + sx
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if matrix_copy[ny][nx] == -1:
                matrix_copy[ny][nx] = dis + 1
                q.append((ny, nx, dis + 1))

    arr.sort(key=lambda x: (x[0], x[1], x[2])) # customers = [(거리, sy, sx)]
    return arr

def bfs2(sy, sx, dy, dx):
    global n

    q = deque([(sy, sx, 0)])
    matrix_copy[sy][sx] = 0
    while q:
        sy, sx, dis = q.popleft()
        if (sy, sx) == (dy, dx):
            return dis

        for i in range(4):
            ny = ddy[i] + sy
            nx = ddx[i] + sx
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if matrix_copy[ny][nx] == -1:
                matrix_copy[ny][nx] = dis + 1
                q.append((ny, nx, dis + 1))
    
    return 999999999

answer = 0
# print(mapping)
for _ in range(m):
    # print("########################")
    matrix_copy = [matrix[i][:] for i in range(n)]
    customers = bfs(taxi_y, taxi_x)
    # print(customers)
    if not customers:
        answer = -1
        break

    dis, sy, sx  = customers[0]
    # print(f"첫번쨰고객:{(sy, sx)}, 거리:{dis}, oil:{oil}")
    if dis > oil:
        answer = -1
        break
    dy, dx = mapping.pop((sy, sx))
    taxi_y, taxi_x = sy, sx
    oil = oil - dis

    matrix_copy = [matrix[i][:] for i in range(n)]
    dis = bfs2(taxi_y, taxi_x, dy, dx)
    # print(f"고객 바래다주고 거리:{dis}, 오일:{oil}")
    if dis > oil:
        answer = -1
        break
    taxi_y, taxi_x = dy, dx
    oil -= dis
    oil += 2 * dis
    # print(f"현재위치:{(taxi_y, taxi_x)} 남은오일:{oil}")

if answer != -1:
    answer = oil

print(answer)
