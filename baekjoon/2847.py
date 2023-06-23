

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst = lst[::-1]
answer = 0
for i in range(n-1):
    
    l = lst[i]
    r = lst[i+1]
    if l <= r:
        dif = r-l+1
        lst[i+1] = l-1
        answer += dif
    
print(answer)