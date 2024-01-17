

n, m = [int(i) for i in input().split()]


stack = [[i,1,[i]] for i in range(n,0,-1)]
sett = set(range(n,0,-1))

while stack:
    out = stack.pop()
    v, l, arr = out[0], out[1], out[2]
    if l == m:
        print(*arr)
    else:
        a = sorted(list(sett - set(arr)), reverse= True)
        for i in a:
            
            stack.append([i,l+1,arr+[i]])







