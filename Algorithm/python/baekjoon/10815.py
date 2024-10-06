
lst = []
for _ in range(4):
    lst.append(list(map(int, input().split())))

a = dict(zip(lst[3], [0]*(lst[2][0])))

for i in set(lst[1]) & set(lst[3]):
    
    a[i] = 1

for i in a.values():
    print(i , end = ' ')
