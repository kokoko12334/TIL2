import sys

input = sys.stdin.readline

a_score = [0] * 101
for i in range(1, 22):
    if i == 1:
        a_score[i] = 5000000
    elif i in [2,3]:
        a_score[i] = 3000000
    elif i in [4,5,6]:
        a_score[i] = 2000000
    elif i in [7,8,9,10]:
        a_score[i] = 500000
    elif i in [11,12,13,14,15]:
        a_score[i] = 300000
    elif i in [16,17,18,19,20,21]:
        a_score[i] = 100000

b_score = [0] * 65
for i in range(1, 32):
    if i == 1:
        b_score[i] = 5120000
    elif i in range(2,4):
        b_score[i] = 2560000
    elif i in range(4,8):
        b_score[i] = 1280000
    elif i in range(8, 16):
        b_score[i] = 640000
    elif i in range(16, 32):
        b_score[i] = 320000

n = int(input())
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    print(a_score[a] + b_score[b])
