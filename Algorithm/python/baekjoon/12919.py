s = input()
t = input()
n = len(s)

answer = 0
def back_tracking(string):
    global s, answer
    if len(string) == n:
        if string == s:
            answer = 1
        return

    if string[-1] == "A":
        back_tracking(string[:-1])
    
    if string[0] == "B":
        back_tracking(string[:0:-1])
back_tracking(t)

print(answer)

