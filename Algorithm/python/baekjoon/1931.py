
import sys
from collections import deque
n = int(sys.stdin.readline())


lst = []
for j in range(n):
    lst2 = [int(i) for i in sys.stdin.readline().split()]
    lst.append(lst2)

end_sor = sorted(lst, key = lambda x: (x[1],x[0]))

end = 0
answer = 0
for i in range(n):
    s = end_sor[i][0]
    e = end_sor[i][1]
    
    if end <= s:
        end = e
        
        answer += 1
print(answer)