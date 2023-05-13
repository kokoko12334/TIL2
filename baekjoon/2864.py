

a,b = input().split()

max_a = a.replace("5", "6")
max_b = b.replace("5", "6")

answer_max = int(max_a) + int(max_b)

min_a = a.replace("6","5")
min_b = b.replace("6","5")

answer_min = int(min_a) + int(min_b)


print(answer_min, answer_max)
