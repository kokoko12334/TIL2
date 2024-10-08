import sys
# 백트랙킹 [무게, 가치, 가성비] 35%에서 시간초과남 12865번 백준
n, k = [int(i) for i in sys.stdin.readline().split()]

lst = []
for _ in range(n):
    
    lst2 = [int(i) for i in sys.stdin.readline().split()]
    lst2.append(round(lst2[1]/lst2[0],10))
    lst.append(lst2)    

lst.sort(key=lambda x: (-x[2],x[0]))


stack = [[0,0,-1]]
temp_maxvalue = 0

while stack:
    out = stack.pop()
    
    total_w = out[0]
    total_v = out[1]
    idx = out[2]
    next_idx = idx +1

    if temp_maxvalue < total_v:
        temp_maxvalue = total_v


    if idx < n-1:
        for i in range(2):
            next_w = total_w + (lst[next_idx][0]*i)
            next_v = total_v + (lst[next_idx][1]*i)

            if next_w > k:
                continue

            
            sol_f =  next_v
            remain_w = k - next_w
            for j in range(next_idx+1, n):
                a = min(remain_w, lst[j][0])
                sol_f += lst[j][2] * a

                remain_w -= a
                if remain_w <= 0:
                    break

            if sol_f <= temp_maxvalue:
                continue

            stack.append([next_w, next_v, next_idx])    

print(temp_maxvalue)





