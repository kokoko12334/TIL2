import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

g = defaultdict(set)

for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    g[a].add(b)
    g[b].add(a)

path = [int(i) for i in input().split()]