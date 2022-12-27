import sys

n, k =map(int, sys.stdin.readline().split())

def minus(x):
    return x-1
def plus(x):
    return x+1
def mul(x):
    return 2*x   
if n == k:
    print(0)
else:    
    enter = True
    lst = []
    sec = 1
    lst.append(minus(n))
    lst.append(plus(n))
    lst.append(mul(n))
    for i in lst:
        if i == k:
            print(sec)
            enter = False

    while enter:
        lst2 = []
        sec += 1
        for i in lst:
            lst2.append(minus(i))
            lst2.append(plus(i))
            lst2.append(mul(i))
        lst = lst2
                   
        for i in lst:
            if i == k:
                print(sec)
                enter = False
                break
            
