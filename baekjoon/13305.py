n = int(input())

d = [int(i) for i in input().split()]

p = [int(i) for i in input().split()]

answer = p[0]*d[0] 
s = p[0]
for i in range(1,n-1):
    if p[i] > s:
        answer += d[i]*s
    else:
        s = p[i]
        answer += d[i]*s

print(answer)