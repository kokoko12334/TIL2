import sys
from collections import deque
input = sys.stdin.readline

n, m, kk = [int(i) for i in input().split()]

arr = [[5]*n for _ in range(n)]

# Input for additional nutrients to be added in winter
add = []
for _ in range(n):
    add.append([int(i) for i in input().split()])

# Initialize tree as a 2D array of deque to store ages of trees in each cell
tree = [[deque() for _ in range(n)] for _ in range(n)]

# Input initial tree positions and ages
for _ in range(m):
    x, y, age = [int(i) for i in input().split()]
    tree[x-1][y-1].append(age)  # Adjust index to 0-based

def spring_and_summer():
    # Simulate spring and summer
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                new_tree = deque()
                dead_tree = 0
                for age in tree[i][j]:
                    if arr[i][j] >= age:  # If enough nutrients
                        arr[i][j] -= age
                        new_tree.append(age + 1)
                    else:
                        dead_tree += age // 2  # Store dead trees' nutrients
                tree[i][j] = new_tree
                arr[i][j] += dead_tree  # Add nutrients from dead trees

def fall():
    # Simulate fall
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(n):
        for j in range(n):
            for age in tree[i][j]:
                if age % 5 == 0:
                    # Tree reproduces
                    for direction in range(8):
                        nx = i + dx[direction]
                        ny = j + dy[direction]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)  # Add a new tree (age 1)

def winter():
    for i in range(n):
        for j in range(n):
            arr[i][j] += add[i][j]

for _ in range(kk):
    spring_and_summer()
    fall()
    winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)
