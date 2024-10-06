def house(k,n):
    globals()['a'+str(0)] = [i for i in range(1, n+1)]
    for o in range(k-1):

        globals()['a'+str(o+1)] = [0]*n
        for j in range(n):
            for i in globals()['a'+str(o)][:j+1]:
                globals()['a'+str(o+1)][j] += i
    lst = globals()['a'+str(k-1)]
    return lst
   
t = int(input())
for _ in range(t):
    k  = int(input())
    n = int(input())
    print(sum(house(k,n)))








T = int(input())

for _ in range(T):
    floor = int(input())
    num = int(input())

    f_list = [i for i in range(1, num+1)]

    for i in range(floor):
        for j in range(1, num):
            f_list[j] += f_list[j-1]
            print(f_list[j], f_list[j-1])

    print(f_list[-1])