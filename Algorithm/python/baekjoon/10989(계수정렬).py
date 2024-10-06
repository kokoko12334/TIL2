import sys
input = sys.stdin.readline
n = int(input())
numbers = [0]*(10001)

for _ in range(n):
    num = int(input())
    numbers[num] += 1

for i in range(1,10001):
    iterr = numbers[i]
    for j in range(iterr):
        print(i)