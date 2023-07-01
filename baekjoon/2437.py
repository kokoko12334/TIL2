import sys
input = sys.stdin.readline

n = int(input())
w = [int(i) for i in input().split()]
w.sort()

answer = 1
for i in w:
    if answer < i:
        break
    answer += i

print(answer)