
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort(reverse= True)
answer = 0
for i in range(n):
    answer += a[i]*b[i]
print(answer)