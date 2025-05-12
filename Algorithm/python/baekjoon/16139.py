import sys

input = sys.stdin.readline

S = list(input())
N = len(S)
q = int(input())

alp = {chr(i):[] for i in range(97, 123)}

for k, prefix in alp.items():
    prefix = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if S[i-1] == k:
            cnt += 1
        prefix[i] = cnt
    alp[k] = prefix        

for _ in range(q):
    a, l, r = [i for i in input().split()]
    l = int(l) + 1
    r = int(r) + 1
    arr = alp[a]
    print(arr[r] - arr[l-1])