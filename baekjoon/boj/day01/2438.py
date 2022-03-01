import time
start = time.time() 
 
n = int(input())
for i in range(1,n+1):
    print('*'*i)
print("time :", time.time() - start) 




start = time.time()  
n = int(input())
for i in range(n):
    print('*'*(i+1))
    
print("time :", time.time() - start) 