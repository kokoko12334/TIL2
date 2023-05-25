
n = int(input())
lst = [int(i) for i in input().split()]


for i in lst:
    if i == 1:
        n-=1
        continue
    num = i
    s = int(i**(1/2))
    for j in range(2,s+1):
        if not num%j:
            n -= 1
            break

print(n)