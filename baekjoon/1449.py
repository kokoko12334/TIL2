n,l = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]
pipe = [0]*(1001)

for i in lst:
    pipe[i] = 1

idx = 0
answer = 0
while idx < 1001:
    if pipe[idx]:
        idx += l
        answer += 1
    else:
        idx += 1

print(answer)

