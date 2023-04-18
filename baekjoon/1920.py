import sys


n = int(sys.stdin.readline())

n_lst = [int(i) for i in sys.stdin.readline().split()]
n_lst.sort()
m = int(sys.stdin.readline())

m_lst = [int(i) for i in sys.stdin.readline().split()]



for i in m_lst:
    s = 0
    e = n - 1
    flag = True    
    while s <= e:
        mid_idx = (s + e) // 2
        mid = n_lst[mid_idx]
        if mid == i:
            flag = False
            print(1)
            break

        if i < mid:
             e = mid_idx-1
        elif i > mid:
            s = mid_idx + 1
    if flag:
        print(0)
