import sys



n,m = [int(i) for i in sys.stdin.readline().split()]

lst = [sys.stdin.readline() for _ in range(n+m)]


sett = set(lst[:n])


cnt = 0
for i in lst[n:]:
    if i in sett:
        cnt += 1

print(cnt)
