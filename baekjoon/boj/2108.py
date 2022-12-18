import sys


n = int(input())


lst = [int(input()) for _ in range(n)]

lst.sort()

print(round(sum(lst)/n))

print(lst[int(n/2)])

fre = []
for i in lst:
    fre.append(lst.count(i))

dicc = dict(zip(lst, fre))
dicc

max(dicc.values())

max(dicc.keys(), key=dicc.values().count)

print(max(lst)-min(lst))


lst
