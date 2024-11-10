from bisect import bisect_right, bisect_left
n, score, p = [int(i) for i in input().split()]
if n == 0:
    print(1)

else:
    lst = [int(i) for i in input().split()][::-1]

    idx = bisect_right(lst, score)
    my_position = n - bisect_left(lst, score) + 1
    rank = n - idx + 1
    if p >= my_position: 
        print(rank)
    else:
        print(-1)