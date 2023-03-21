
# [+ , - , * , /]
n = int(input())

numbers = [int(i) for i in input().split()]

operators = [int(i) for i in input().split()]

stack = [[numbers[0],0,operators]]

minn = 999999999999999
maxx = -999999999999999
while stack:
    out = stack.pop()
    
    num = out[0]
    idx = out[1]
    op = out[2]
    if idx < n-1:  
        for i in range(4):
            copy = [i for i in op]
            if i == 0 and op[i] >= 1:
                next = num + numbers[idx+1]
                
                copy[i] -= 1
                stack.append([next, idx+1, copy])
            elif i== 1 and op[i] >=1:
                next = num - numbers[idx+1]
               
                copy[i] -= 1
                stack.append([next, idx+1, copy])
            elif i == 2 and op[i] >= 1:
                next = num * numbers[idx+1]
               
                copy[i] -= 1    
                stack.append([next, idx+1, copy])
            elif i == 3 and op[i] >=1:
                next = int(num/numbers[idx+1])
                 
                copy[i] -= 1
                stack.append([next, idx+1, copy])    
    else:
        
        if num > maxx:
            maxx = num
        if num < minn:
            minn = num


print(maxx)
print(minn)

