from itertools import combinations
from math import sqrt

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
    x_total = 0
    y_total = 0
    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        vectors.append([x, y])
        x_total += x
        y_total += y
        
    end_dots = list(combinations([int(i) for i in range(n)], n//2))
    result = float("inf")
    # print(end_dots)
    nn = len(end_dots)//2
    for idx_list in end_dots[:nn]:
        x_tmp = 0
        y_tmp = 0
        for idx in idx_list:
            x, y = vectors[idx]
            x_tmp += x
            y_tmp += y
        
        start_x_sum = x_total - x_tmp
        start_y_sum = y_total - y_tmp
        
        x_tmp -= start_x_sum
        y_tmp -= start_y_sum
        
        result = min(result, sqrt(x_tmp**2 + y_tmp**2))
        # print(result)
        
    print(f"{result:.15f}")