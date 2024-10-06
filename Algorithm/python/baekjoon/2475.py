
lst=  [int(i) for i in input().split()]

answer = 0
for i in lst:
    answer += (i**2)
print(answer%10)
