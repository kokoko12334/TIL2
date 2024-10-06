
lst = [1, 2, 3, 4, 5, 6]


def cases(leng, n):

    cnt = 1
    s = leng
    up = 1
    while cnt <= n:
        up *= s
        s -= 1
        cnt += 1

    down = 1
    for i in range(1, n+1):

        down *= i

    return int(up/down)


def combination(lst, n):

    for i in range(len(lst)):

        for j in lst[i+1:]:

            print(lst[i], j)
    print(cases(len(lst), n))


combination(lst, 2)


cases(5, 2)

