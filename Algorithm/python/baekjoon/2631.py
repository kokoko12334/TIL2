from bisect import bisect_left
n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))


lis = [lst[0]]

cnt = 1
for i in range(1,n):
    num = lst[i]
    if lis[-1] < num:
        cnt += 1
        lis.append(num)
    else:
        idx = bisect_left(lis,num)
        lis[idx] = num


print(n-cnt)