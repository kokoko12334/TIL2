
num = int(input())

lst =[]
for i in range(1,1000001):
    each_num = [int(j) for j in list(str(i))]
    
    lst.append(sum(each_num)+i)

data = dict(zip(range(1,1000001),lst))
data

gener = [k for k, v in data.items() if v==num]

if len(gener) != 0:
    print(min(gener))
else:
    print(0)





#########쉬운것
n = int(input())

for x in range(1, n + 1):
    nlist = [int(y) for y in str(x)]

    if int(sum(nlist) + x) == n: 
        print(x)
        break
        
    if x == n:
        print(0)
        