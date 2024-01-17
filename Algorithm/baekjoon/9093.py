import sys

num = int(sys.stdin.readline())

test = [sys.stdin.readline().split() for _ in range(num)]


for i in test:
    start = ''
    for j in i:
        start += j[::-1]+' '
    print(start)
