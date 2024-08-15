from collections import deque
#f: 건물층, s:현재위치, g:목표, u: 업, d:다운
f, s, g, u, d = [int(i) for i in input().split()]

seen = [-1] * (f+1)

q = deque([(s, 0)])
seen[s] = 0

while q:
    current, cnt = q.popleft()
    for i in [u, -d]:
        next_ = current + i
        if next_ <= 0 or next_ > f:
            continue

        if seen[next_] == -1:
            seen[next_] = cnt+1
            q.append((next_, cnt+1))

if seen[g] == -1:
    print('use the stairs')
else:
    print(seen[g])



