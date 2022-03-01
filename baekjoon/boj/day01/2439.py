n = int(input())
for i in range(1,n+1):
    r = '*'*i
    print(r.rjust(n))



#######다른 풀이
n = int(input())
for i in range(n):
    
    print(' '*(n-i-1)+'*'*(i+1))







