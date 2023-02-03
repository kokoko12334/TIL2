num = int(input())

test3 = num//3

test5 = num//5


lst = []
for i in range(test3+1):
    for j in range(test5+1):
        if 3*i+5*j ==num:
            lst.append(i+j)
if len(lst) !=0:
    print(min(lst))
else:
    print(-1)


######DP로 풀기
num = int(input())
dp = {}  #dp

lst = [0]  #초기값

level = 0
result = False
while min(lst) < num:
    result = True
    lst2 = []
    for i in lst:
        if i in dp.keys():
            pass
        else:
            child = [i+3, i+5]
            dp[i] = child
            lst2 += child
    level += 1
    lst = set(lst2)
    if num in lst:
        result = False
        break

if result:
    print(-1)

else:
    print(level)








