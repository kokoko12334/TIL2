num = int(input())


def c_sum(n):
    result = (3*n+6)*(n-1)+7
      
    return result   


if num ==1:
    print(1)
 
else:
  
    i = 1
    
    e = c_sum(i)
    while num > e:
        i += 1
        e = c_sum(i)
    print(i+1)


