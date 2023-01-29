import sys



n = int(sys.stdin.readline())

n_lst = [int(i) for i in sys.stdin.readline().split()]

m = int(sys.stdin.readline())

m_lst = [int(i) for i in sys.stdin.readline().split()]


n_lst = set(n_lst)
for i in m_lst:
    
    if i in n_lst:
        print(1)
    else:
        print(0)