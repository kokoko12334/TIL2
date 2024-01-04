s = input()
t = input()

answer = 0

while True:

    alphabet = t[-1]

    if alphabet == "A":
        t = t[:-1]

    else:

        t = t[:-1]
        t = t[::-1]

    if len(s) == len(t):

        if s == t:
            answer = 1
        break

print(answer)