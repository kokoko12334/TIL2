

































######정답
numbers = list(map(int, input().split()))

# Bubble sort
for i in range(len(numbers) - 1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            print(*numbers)

		# 효율성을 위한 탈출 조건
    if numbers == [1, 2, 3, 4, 5]:
        break
