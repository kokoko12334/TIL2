# https://seongonion.tistory.com/130
import sys

arr = [int(sys.stdin.readline()) for _ in range(int(input()))]
count = [0] * (max(arr) + 1)

for num in arr:
    count[num] += 1

# print(count)

for i in range(1, len(count)):
    count[i] += count[i-1]

# print(count)

result = [0] * (len(arr))

for num in arr:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1

print(*result, sep='\n')
