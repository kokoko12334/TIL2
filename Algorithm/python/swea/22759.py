import sys

input = sys.stdin.readline

n = int(input())
    
# 최대값 + 1에서 기준선만 넘으면

for _ in range(n):
    l, r = [int(i) for i in input().split()]

    standard = (r + 1)/2

    if standard <= l:
        print("yes")
    else:
        print("no")

if 1:
    pass
