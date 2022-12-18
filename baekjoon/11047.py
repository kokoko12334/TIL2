# import sys
# sys.stdin.readline()

n, k = map(int, input().split())

lst = [int(input()) for _ in range(n)]

cnt = 0
stop = False
for i in lst[::-1]:
    
    k -= i
    
    while k >= 0:
        k += i
        
        if k == 0:
            stop = True
            break
        coins = int(k/i)
        
        k = k-(i*(coins+1))
        cnt += coins

    if stop:
        break    
        
    k += i
print(cnt)
