
n = int(input())
m = int(input())
no = set()
if m:
    no = set(input().split())

nn = len(str(n))

arr = []
minn = abs(n - 100)
for i in range(1000001):
    num = str(i)
    flag = True
    for j in num:
        if j in no:
            flag = False
            break
    if flag:
        minn = min(minn, len(num) + abs(n - int(num)))

print(minn)
