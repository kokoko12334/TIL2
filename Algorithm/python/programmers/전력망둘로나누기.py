from collections import defaultdict
def solution(n, wires):
    answer = float("inf")
    for i in range(n-1):
        g = defaultdict(list)
        for j in range(n-1):
            if i == j:
                continue
            a,b = wires[j]
            g[a].append(b)
            g[b].append(a)

        stack = [1]
        seen = [0]*(n+1)
        seen[1] = 1
        cnt = 0
        while stack:
            cnt += 1
            v = stack.pop()
            for k in g[v]:
                if seen[k] == 0:
                    stack.append(k)
                    seen[k] = 1
        # print(g, n, cnt)
        cnt2 = n-cnt
        answer = min(answer,abs(cnt-cnt2))
    
    return answer