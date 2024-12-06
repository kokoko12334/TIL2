
for test in range(10):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    matrix = [[0] * n for _ in range(255)]
    for i in range(2, n - 2):
        height = arr[i]
        for j in range(height):
            matrix[j][i] = 1

    answer = 0
    for i in range(2, n - 2):
        for h in range(255):
            flag = True
            if not matrix[h][i]:
                continue

            for diff in [-2, -1, 1, 2]:
                if matrix[h][i + diff]:
                    flag = False
                    break
            if flag:
                answer += 1
    
    print(f"#{test + 1} {answer}")




