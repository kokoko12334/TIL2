a = int(input())

for i in range(1, a+1):
    r = '*'*i
    
    print(r.rjust(a))   #rjust는 반환값이라서 print에 넣어야함.


