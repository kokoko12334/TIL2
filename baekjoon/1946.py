import sys

n = int(sys.stdin.readline())


for _ in range(n):
    test = int(sys.stdin.readline())
    lst = []
    answer = test
    for _ in range(test):
        p, i = [int(i) for i in sys.stdin.readline().split()]
        lst.append([p,i])
        
    lst.sort(key= lambda x: x[0])
    answer = 1
    k = 0
    for i in range(1,test):
        if lst[i][1] < lst[k][1]:
            answer += 1
            k = i
    print(answer)


    