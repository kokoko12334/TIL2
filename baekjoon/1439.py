n = input()

zip_arr = []
stack= [n[0]]

for i in range(1, len(n)):
    if stack[0] == n[i]:
        pass
    else:
        out = stack.pop()
        zip_arr.append(out)
        stack.append(n[i])
zip_arr.append(stack.pop())

one = zip_arr.count('1')
zero = zip_arr.count('0')

print(min(one,zero))

