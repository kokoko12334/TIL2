
from itertools import product
n = int(input())

m = [int(i) for i in input().split()]

op = [int(i) for i in input().split()]


def summ(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    num = a//b
    if num < 0:
        result = -(-a//b)
    else:
        result = a//b
    return result


lst = [4, 5, 6]

s = lst[0]
for i in lst[1:]:
    s = summ(s, i)
    s = div(s,)
print(s)


div()


case = [1, 0, 1, 0]


for i in case:
    n = i
    for j in


result = list(product(case, 'a'))


print(len(result))

result
