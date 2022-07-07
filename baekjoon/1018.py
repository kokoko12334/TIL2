import sys

chess_B = []
for i in range(8):
    if i % 2 == 0:
        chess_B.append('BWBWBWBW')
    else:
        chess_B.append('WBWBWBWB')

chess_W = []
for i in range(8):
    if i % 2 == 0:
        chess_W.append('WBWBWBWB')
    else:
        chess_W.append('BWBWBWBW')

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(n)]

# 모든 경우의 수 탐색
lst = []
for i in range(7, n):

    end_i = i - 7

    for j in range(7, m):
        end_j = j - 7
        lst2 = []
        for k in range(end_i, i+1):
            lst2.append(board[k][end_j: j+1])
        lst.append(lst2)


def b(lst):
    cnt = 0
    for j in range(8):
        for k in range(8):
            if lst[j][k] != chess_B[j][k]:
                cnt += 1
    return cnt


def w(lst):
    cnt = 0
    for j in range(8):
        for k in range(8):
            if lst[j][k] != chess_W[j][k]:
                cnt += 1
    return cnt


result = []
for i in range(len(lst)):

    result.append(b(lst[i]))
    result.append(w(lst[i]))

print(min(result))
