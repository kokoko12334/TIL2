import sys
from collections import deque
k = int(sys.stdin.readline())


for _ in range(k):
    v, e = [int(i) for i in sys.stdin.readline().split()]
    g = {i:[] for i in range(1,v+1)}

    for _ in range(e):
        a,b = [int(i) for i in sys.stdin.readline().split()]
        g[a].append(b)
        g[b].append(a)

    all_cases = set(range(1,v+1))
    q = deque([1])
    seen = [0]* (v+1)
    seen[1] = 1
    seen2 = {1}
    flag = True
    while q:
        out = q.popleft()
        v = out

        for i in g[v]:
            if seen[i] == 0:
                q.append(i)
                seen[i] = seen[v] * -1
                seen2.add(i)
            else:
                if seen[i] == seen[v]:
                    flag = False
                    q = []
                    break
        
        if not q and flag:
            b = all_cases - seen2
            if b:
                a = list(b)[0]
                q.append(a)
                seen[a] = 1
                seen2.add(a)

    if flag:
        print("YES")
    else:
        print("NO")

