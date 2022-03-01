
import time
start = time.time() 

n = int(input())

for i in range(1,n+1):
    r = '*'*n
    r=' '.join(list(r))
    if i%2 !=0:
        print(r)
    else:
        print(r.rjust(n*2))

print("time :", time.time() - start) 

########다른 풀이
start = time.time()

n = int(input())

for i in range(1,n+1):
    if i%2 !=0:
        print('* '*n)
    else:
        print(' *'*n)

print("time :", time.time() - start) 


####다른풀이 222
n = int(input())
for i in range(n):
    print('* ' * n if i % 2 == 0 else' *' * n)

#print(출력값 / if true면 앞의 출력값 출력 / else 그외의 출려값)










