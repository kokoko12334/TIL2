matrix = []
for i in range(9):
    a = int(input())
    matrix.append(a)

max_value = max(matrix)
max_index = matrix.index(max_value)+1

print(max_value)
print(max_index)



