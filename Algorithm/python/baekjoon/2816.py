import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(input().strip("\n"))

answer = []
# print(arr)

def cal(string, idx):

    string = arr.index(string)

    for _ in range(string - 0):
        answer.append("1")

    for i in range(string, idx, -1):
        arr[i], arr[i-1] = arr[i-1], arr[i]
        answer.append("4")
    # print(arr)
    # print(answer)


cal("KBS1", 0)
cal("KBS2", 1)

print("".join(answer))