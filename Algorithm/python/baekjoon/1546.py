a = int(input())

lst = list(map(int, input().split()))

lst.sort()

M=lst[-1]

lst2 = [i/M*100 for i in lst]
result = sum(lst2)/a
print((round(result, 6)))


