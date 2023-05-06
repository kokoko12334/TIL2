


n = int(input())

answer = [0,0,0]

f = n//300
n = n%300
answer[0] = f

h = n//60
n = n%60
answer[1] = h

t = n//10
n = n%10
answer[2] = t

if not n:
    print(*answer)
else:
    print(-1)




