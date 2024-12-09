
# 6혹은 끝까지
# 1,2,3,4,5라면 카운트 안함 0인경우만
# 각각의 케이스를 조사하여(인덱스로 표시)
# {(0,1),(0,2)}, {(2,2), (2,3)} -> 커버 되는 것 이거의 합이 최대가 되는 것 모든 경우의 수 중에서 합이 최대
# DFS로 구현

n, m = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

# n, m = 4, 6

# matrix = [
#     [0, 0, 0, 0, 0, 0],
#     [0, 5, 0, 0, 0, 0],
#     [0, 0, 1, 0, 6, 0],
#     [0, 0, 0, 0, 0, 0],
# ]

# [{(0,1), (0,3)}, {(1,1),(2,2)}]
# 오른쪽은  m - 1까지, 왼쪽은 0, 위쪽은 0, 아래는 n - 1
def cal_case(i, j):
    num = matrix[i][j]
    cases = []
    if num == 1:
        sett = set() # 오른쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cases.append(sett)

        sett = set() # 왼쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cases.append(sett)

        sett = set() # 아래
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cases.append(sett)

        sett = set() # 위
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cases.append(sett)
        return cases
    
    elif num == 2:
        sett = set()
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cases.append(sett)

        sett = set()
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cases.append(sett)

        return cases
    elif num == 3:

        sett = set() # 위
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cases.append(sett)

        sett = set() # 오른쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cases.append(sett)


        sett = set() # 아래
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cases.append(sett)


        sett = set() # 왼쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cases.append(sett)

        return cases
    
    elif num == 4:
        sett = set() # 왼쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cases.append(sett)


        sett = set() # 위
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cases.append(sett)

        sett = set() # 오른쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cases.append(sett)

        sett = set() # 아래
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cases.append(sett)
        return cases
    
    elif num == 5:
        sett = set() # 오른쪽
        cur_i, cur_j = i, j
        while True:
            if cur_j >= m or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j += 1
        cur_i, cur_j = i, j
        while True:
            if cur_j < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_j -= 1
        cur_i, cur_j = i, j
        while True:
            if cur_i >= n or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i += 1
        cur_i, cur_j = i, j
        while True:
            if cur_i < 0 or matrix[cur_i][cur_j] == 6:
                break
            if matrix[cur_i][cur_j] == 0:
                sett.add((cur_i, cur_j))
            cur_i -= 1
        cases.append(sett)
        return cases


cases = dict()
for i in range(n):
    for j in range(m):
        if matrix[i][j] in {1, 2, 3, 4, 5}:
            result = cal_case(i, j)
            cases[(i,j)] = result
            

# (0, 1): [{(0,1), (0,3)}, {(1,1),(2,2)}]
# (0, 2): [{(0,1), (0,3)}, {(1,1),(2,2)}]

keys = list(cases.keys())
arr = []
cover = 0
def dfs(idx):
    global cover
    if idx == len(keys):
        sett = set()
        for i in arr:
            sett.update(i)
        cover = max(cover, len(sett))
        return

    for c in cases[keys[idx]]:
        arr.append(c)
        dfs(idx + 1)
        arr.pop()

dfs(0)

answer = n * m
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            answer -= 1

print(answer - cover)



