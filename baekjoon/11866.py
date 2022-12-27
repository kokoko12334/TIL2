import sys

n,k = [int(i) for i in sys.stdin.readline().split()]

lst = list(range(1,n+1))
k_idx = k-1
result = []
while True:
    result.append(lst[k_idx])
    lst = lst[k:]+lst[:k_idx]
   
    if k>len(lst):
        break


while len(lst) != 0:
    
    if len(lst) != 1:
        a = k_idx%len(lst)
        result.append(lst[a])
        lst = lst[a+1:]+lst[:a]
    else:
        result.append(lst[0])
        break

print('<', end = '')
for i in result[:-1]:
    print(str(i), end = ', ')
print(result[-1], end = '')    
print('>')    


