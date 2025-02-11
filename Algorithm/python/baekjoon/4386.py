n = int(input())

starts = []
for _ in range(n):
    y, x = [float(i) for i in input().split()]
    starts.append([y, x])

def search(idx):
    total = 0
    y, x = starts[idx][0], starts[idx][1]
    seen = {i for i in range(n)}
    seen.remove(idx)

    stack = [(y, x)]
    while stack:
        y, x = stack.pop()

        current = [float("inf"), -1]
        for i in seen:
            ny, nx = starts[i]

            dis = ((ny - y)**2 + (nx - x)**2)**(1/2)

            if current[0] > dis:
                current = [dis, i]
        
        next_idx = current[1]
        total += current[0]

        seen.remove(next_idx)
        stack.append((starts[next_idx][0], starts[next_idx][1]))
        if not seen:
            break

    return total

answer = float("inf")
for i in range(n):
    answer = min(answer, search(i))

print(format(answer, ".2f"))