

n = int(input())
lst = [int(i) for i in input().split()]
lst2 = lst[::-1]

dp1 = [1]*(n)
dp2 = [1]*(n)


for i in range(1,n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

        if lst2[i] > lst2[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
        

answer = 0
for i in range(n):
    a = dp1[i] + dp2[::-1][i]
    if answer <a:
        answer = a
print(answer-1)




