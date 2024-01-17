import sys

num = int(sys.stdin.readline())

lst = []
for _ in range(num):
    a = int(sys.stdin.readline())

    if a != 0:
        lst.append(a)
    else:
        del lst[-1]
        
print(sum(lst))
