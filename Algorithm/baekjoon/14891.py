from collections import deque
import sys
input = sys.stdin.readline

lst = []
for _ in range(4):
    lst.append(deque([int(num) for num in list(input())[:-1]]))

k = int(input())

for _ in range(k):
    idx, d = [int(i) for i in input().split()]
    idx -= 1

    stack = [(idx, d)]
    seen = [0] * 4
    seen[idx] = 1
    while stack:
        idx, d = stack.pop()

        l = idx - 1
        l_move = 0
        r = idx + 1
        r_move = 0

        if l >= 0 and lst[l][2] != lst[idx][6]:
            l_move = d * -1
        if r < 4 and lst[r][6] != lst[idx][2]:
            r_move = d * -1
    
        if d == -1:
            num = lst[idx].popleft()
            lst[idx].append(num)
        else:
            num = lst[idx].pop()
            lst[idx].appendleft(num)
        
        if l_move != 0 and not seen[l]:
            stack.append((l, l_move))
            seen[l] = 1
        if r_move != 0 and not seen[r]:
            stack.append((r, r_move))
            seen[r] = 1

answer = 0
for i in range(4):
    if lst[i][0]:
        answer += 2**(i)

print(answer)