
n,m = [int(i) for i in input().split()]

A = [[int(i) for i in input()] for _ in range(n)]    
B = [[int(i) for i in input()] for _ in range(n)]    


cnt = 0
for i in range(n):
    for j in range(m):
        if i+2 >= n or j+2 >= m:
            continue
        if A[i][j] != B[i][j]:
            cnt += 1
            for k in range(3):
                for p in range(3):
                    if A[i+k][j+p]: 
                        A[i+k][j+p] -= 1
                    else:
                        A[i+k][j+p] += 1


flag = False
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            flag = True
            break
    if flag:
        break

if flag:
    print(-1)
else:
    print(cnt)
