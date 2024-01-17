import sys

n = int(sys.stdin.readline())

n_lst = [int(i) for i in sys.stdin.readline().split()]

m = int(sys.stdin.readline())

m_lst = [int(i) for i in sys.stdin.readline().split()]


set_lst= set(n_lst) | set(m_lst)

num_count = {}

for i in set_lst:
    num_count[i] = 0


for i in n_lst:
    num_count[i] += 1


answer = [num_count[i] for i in m_lst]

print(*answer)
