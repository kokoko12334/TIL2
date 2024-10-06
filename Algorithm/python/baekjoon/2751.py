import sys


lst = [int(sys.stdin.readline()) for _ in range(int(input()))]

print(*sorted(lst), sep = '\n')


