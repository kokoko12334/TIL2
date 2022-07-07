import sys


num = int(sys.stdin.readline())


test = [sys.stdin.readline() for _ in range(num)]

for i in test:
    i = i.rstrip('\n')
    if len(i) % 2 == 1:
        print('NO')
    else:
        n = int(len(i)/2)
        for _ in range(n):
            i = i .replace('()', "")
        if i == "":
            print("YES")
        else:
            print('NO')
