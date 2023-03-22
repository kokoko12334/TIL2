
n = int(input())

lst = [int(i) for i in input().split()]

lst.sort()

total = 0
c = 0

for i in lst:
    
    c += i
    total += c
    
print(total)



