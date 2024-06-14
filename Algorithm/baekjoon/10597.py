import sys
sys.setrecursionlimit(10**6)
num_string = input()

str_len = len(num_string)

quo = str_len // 9

if str_len <= 9:
    n = str_len
else:
    remain = str_len - 9
    n = 9 + (remain // 2)

arr = []
seen = [0] * (n+1)

def back(index, arr):

    if index == str_len:
        print(*arr)
        return True

    num = int(num_string[index])
    if not seen[num]:
        seen[num] = 1
        arr.append(num)
        result = back(index + 1, arr)
        if result:
            return
        seen[num] = 0
        arr.pop()
    
    if index + 1 < str_len:
        num2 = int(num_string[index:index+2])
        if num2 <= n and not seen[num2]:
            seen[num2] = 1
            arr.append(num2)
            result = back(index + 2, arr)
            if result:
                return
            seen[num2] = 0
            arr.pop()

back(0, [])