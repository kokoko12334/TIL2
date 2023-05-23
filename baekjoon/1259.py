
while True:
    num = input()
    if not int(num):
        break
    iterr = len(num)//2
    num2 = num[::-1]
    answer = True
    
    for i in range(iterr):
        if num[i] != num2[i]:
            answer = False
            break
    if answer:
        print("yes")
    else:
        print("no")