import heapq
import sys

input = sys.stdin.readline
n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
result = 0

while len(card) > 1:
    a, b =  heapq.heappop(card), heapq.heappop(card)
    result += a + b
    heapq.heappush(card, a + b)

print(result)
