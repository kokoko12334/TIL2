a = int(input())


for i in range(a):
    b, c = map(int, input().split())

    r = b + c
    print(f'Case #{i+1}: {b} + {c} = {r}')