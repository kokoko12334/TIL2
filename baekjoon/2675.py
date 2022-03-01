a = int(input())

for i in range(a):
    num, st = input().split()
    num = int(num)
    r = ''
    for j in range(len(st)):
        r += st[j]*num
    print(r)





