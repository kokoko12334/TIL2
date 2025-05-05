from itertools import permutations
from math import sqrt

def dfs(i):
    global n

    if len(case) == (n // 2):
        all_cases.append(case[:])
        return

    for j in range(i + 1):
        next_ = idxes[j]
        flag = True
        for num in next_:
            if seen[num]:
                flag = False
                break

        if flag:
            for idx in next_:
                seen[idx] = 1
            case.append(next_)
            dfs(j)
            case.pop()
            for idx in next_:
                seen[idx] = 0


def caculate(case):
    v = [0, 0]
    for c in case:
        v1 = vectors[c[0]]
        v2 = vectors[c[1]]
        v[0] += v1[0] - v2[0]
        v[1] += v1[1] - v2[1]
    return sqrt(v[0] ** 2 + v[1] ** 2)


T = int(input())

for _ in range(T):
    n = int(input())

    vectors = []
    for _ in range(n):
        vectors.append([int(i) for i in input().split()])

    idxes = list(permutations([int(i) for i in range(n)], 2))
    nn = len(idxes)
    all_cases = []
    for i in range(nn):
        seen = [0] * n
        stack = [idxes[i]]
        for idx in idxes[i]:
            seen[idx] = 1
        case = [idxes[i]]
        dfs(i)

    answer = float("inf")
    for case in all_cases:
        answer = min(answer, caculate(case))
    print(f"{answer:.15f}")