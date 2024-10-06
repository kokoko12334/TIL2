import sys
n = int(sys.stdin.readline())
lst = []

cnt = 1
i = 1

while cnt <= n:

    if '666' in str(i):
        lst.append(i)
        cnt += 1
        i += 1
    else:
        i += 1

print(lst[-1])
