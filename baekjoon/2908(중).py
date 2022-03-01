a1 , a2 = input().split()
def trans(x):
    lst = list(x)
    lst2 = lst.copy()
    for i in range(len(lst)):
        lst[i] = lst2[-(i+1)]
    
    r=int(''.join(lst))
    
    return r


b1 = trans(a1) ; b2 = trans(a2)
lst = []
lst.append(b1) ; lst.append(b2)

print(max(lst))

########
a,b = map(int,input().split())

c = int(str(a)[::-1])
d = int(str(b)[::-1])
if c > d:
    print(c)
if c < d:
    print(d)


