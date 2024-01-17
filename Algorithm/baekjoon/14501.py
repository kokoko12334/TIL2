
#11:15
import sys

n = int(sys.stdin.readline())



lst = []
for i in range(n):
    end, value = [int(i) for i in sys.stdin.readline().split()]
    lst.append([i+1,end, value])



#######dfs
result = 0
for i in range(n):
    
    stack = [lst[i]]
    seen = {lst[i][0]}
    answer = [0]
    while stack:
        out = stack.pop()
        
        s,e,v = out[0],out[1],out[2]
        
        next = s + e
        if next == n+1:
            answer.append(v)
            
        for j in range(next-1, n):
            if lst[j][0] +lst[j][1] > n+1:
                answer.append(v)
                continue
            
                
            stack.append([lst[j][0],lst[j][1], v+lst[j][2]])
    maxx = max(answer)
    if maxx > result:
        result = maxx
    
print(result)





