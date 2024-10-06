#테스트 케이스
#문서의 수 m번째 문서 -> 출력은 몇번만에 출력되는지
#중요도 순서

import sys
from collections import deque

test = int(sys.stdin.readline())


for _ in range(test):
    n,m = map(int, sys.stdin.readline().split())
    lst = [int(i) for i in sys.stdin.readline().split()]
    cnt = 0
    all_same = True
    while sum(lst)/len(lst) != max(lst):
        f_idx = lst.index(max(lst))
        v = lst[m] #물건확인
        lst[m] = '*'  #포장하고
        lst = lst[f_idx:]+lst[:f_idx]  #이사하고
       
             
        que = deque(lst)
        
        cnt += 1
        m = lst.index('*') #이사위치 확인
        que.popleft()
        if m == 0:
            print(cnt)
            all_same = False
            break
        lst = list(que)
        m = lst.index('*') #이사위치 확인
        lst[m] = v #이사 풀고
        

    
    if all_same:
        print(cnt+m+1)


