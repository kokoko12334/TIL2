
import sys

n,l = [int(i) for i in sys.stdin.readline().split()]

lst = [[int(i) for i in sys.stdin.readline().split()]for _ in range(n)]
stack = []

total = n*2
for i in range(n):
    seen = [True]*n
    s = [lst[0][i],0]
    stack.append(s)
    while stack:
        out = stack.pop()
        
        v,idx = out[0], out[1]
        if idx < n - 1:
            if lst[idx+1][i] == v:
                stack.append([lst[idx+1][i], idx+1])
            elif lst[idx+1][i] == v - 1:
                seen[idx+1] = False
                flag = True
                for j in range(2,l+1):
                    if idx+j >= n:
                        flag = False
                        total -= 1
                        break
                    if not seen[idx+j] or lst[idx+j][i] != v-1:
                        flag = False
                        total -= 1
                        break
                    else:
                        seen[idx+j] = False
                if flag:
                    stack.append([lst[idx+l][i],idx+l])
            elif lst[idx+1][i] == v+1:
                
                flag = True
                if not seen[idx]:
                    total -= 1
                else:
                    seen[idx] = False
                    for j in range(1,l):
                        if idx -j < 0:
                            flag = False
                            total -= 1
                            break
                        if not seen[idx-j] or lst[idx-j][i] != v:
                            flag = False
                            total -= 1
                            break
                        else:
                            seen[idx-j] = False
                    if flag:
                        stack.append([lst[idx+1][i], idx+1])
            else:
                total -= 1

for i in range(n):
    seen = [True]*n
    s = [lst[i][0], 0]
    stack.append(s)
    while stack:
        out = stack.pop()

        v, idx = out[0], out[1]
        if idx < n - 1:
            if lst[i][idx+1] == v:
                stack.append([lst[i][idx+1], idx+1])
            elif lst[i][idx+1] == v - 1:
                seen[idx+1] = False
                flag = True
                for j in range(2, l+1):
                    if idx+j >= n:
                        flag = False
                        total -= 1
                        break
                    if not seen[idx+j] or lst[i][idx+j] != v-1:
                        flag = False
                        total -= 1
                        break
                    else:
                        seen[idx+j] = False
                if flag:
                    stack.append([lst[i][idx+l], idx+l])
            elif lst[i][idx+1] == v+1:
                
                flag = True
                if not seen[idx]:
                    total -= 1
                else:
                    seen[idx] = False
                    for j in range(1, l):
                        if idx - j < 0:
                            flag = False
                            total -= 1
                            break
                        if not seen[idx-j] or lst[i][idx-j] != v:
                            flag = False
                            total -= 1
                            break
                        else:
                            seen[idx-j] = False
                    if flag:
                        stack.append([lst[i][idx+1], idx+1])
            else:
                total -= 1



print(total)
