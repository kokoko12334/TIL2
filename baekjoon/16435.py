n,l = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]

lst.sort()

for i in lst:
    
    if i <= l:
        l += 1
    else:
        break

print(l)