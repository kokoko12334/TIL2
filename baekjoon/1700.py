from collections import deque
n, k = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]

plug = deque()
answer = 0
for i in range(k):
    
    if lst[i] in plug:
        continue
    
    elif lst[i] not in plug and len(plug)<n:
        plug.append(lst[i])
    
    else:
        # value, idx
        later = [-1,-1]
        for j in plug:
            try:
                idx = lst[i+1:].index(j)
            except:
                idx = 999    
            if idx > later[1]:
                later = [j, idx]
                
        plug.remove(later[0])
        answer += 1
        plug.append(lst[i])

print(answer)