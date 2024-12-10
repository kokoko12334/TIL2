import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n ,m, k = [int(i) for i in input().split()]

matrix = []
for _ in range(3):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

def r_operation():
    max_len = 0
    for i in range(len(matrix)):
        arr = matrix[i]
        number_cnt = dict()
        arr.sort(reverse = True)
        for _ in range(len(arr)):
            num = arr.pop()
            if num == 0:
                continue
            if num in number_cnt:
                number_cnt[num] += 1
            else:
                number_cnt[num] = 1
        hq = []
        for k, v in number_cnt.items():
            heappush(hq, (v, k))

        while hq:
            count, number = heappop(hq)
            arr.append(number)
            arr.append(count)
        max_len = max(max_len, len(arr))

    max_len = min(100, max_len)
    for i in range(len(matrix)):
        arr = matrix[i]
        diff = max_len - len(arr)
        for _ in range(diff):
            arr.append(0)

def c_operation():
    max_len = 0
    temp = []
    for i in range(len(matrix[0])):
        arr = []
        for j in range(len(matrix)):
            arr.append(matrix[j][i])
        number_cnt = dict()
        arr.sort(reverse = True)
        for _ in range(len(arr)):
            num = arr.pop()
            if num == 0:
                continue
            if num in number_cnt:
                number_cnt[num] += 1
            else:
                number_cnt[num] = 1
        hq = []
        for k, v in number_cnt.items():
            heappush(hq, (v, k))

        while hq:
            count, number = heappop(hq)
            arr.append(number)
            arr.append(count)
        temp.append(arr)
        max_len = max(max_len, len(arr))

    for i in range(len(temp)):
        arr = temp[i]
        diff = max_len - len(arr)
        for _ in range(diff):
            arr.append(0)
    
    max_len = min(100, max_len)
    temp_c = max_len
    temp_r = len(temp)
    temp_matrix = [[] for _ in range(temp_c)]
    for i in range(temp_r):
        arr = temp[i]
        for j in range(temp_c):
            temp_matrix[j].append(arr[j])
    return temp_matrix

cnt = 0
while True:
    if n - 1 < len(matrix) and m - 1 < len(matrix[0]) and matrix[n-1][m-1] == k:
        break
    if cnt > 100:
        break

    col = len(matrix)
    row = len(matrix[0])

    if col >= row:
        r_operation()
    else:
        matrix = c_operation()
    cnt += 1

if cnt <= 100:
    print(cnt)
else:
    print(-1)