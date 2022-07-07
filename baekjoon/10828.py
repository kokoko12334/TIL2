import sys

num = int(sys.stdin.readline())

command = [sys.stdin.readline().split() for _ in range(num)]

lst = []

for i in command:
    if i[0] == 'push':
        lst.append(int(i[1]))
    elif i[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(int(lst.pop()))
    elif i[0] == 'size':
        print(len(lst))
    elif i[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
