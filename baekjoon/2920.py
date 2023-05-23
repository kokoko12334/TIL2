
lst = [int(i) for i in input().split()]

n = 8
result = []
for i in range(n-1):
    result.append(lst[i+1] - lst[i])


asc = result.count(1)
des = result.count(-1)


if asc == 7:
    print("ascending")
elif des == 7:
    print("descending")
else:
    print("mixed")
