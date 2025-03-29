
lst = []

for _ in range(10):
    lst.append(int(input()))

sum_lst = [0] * 11
for i in range(1, 11):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]

answer = float("inf")
close100 = float("inf")
for i in range(1, 11):
    summ = sum_lst[i] - sum_lst[0]
    num = abs(summ - 100)

    if num < close100:
        answer = summ
        close100 = num
    elif num == close100:
        if summ > answer:
            answer = summ
print(answer)