# from time import time

import time


def some(x):
    return x
n = 10**5
strings = ["x"]*n
start = time.time()
s = ""
for x in strings:
    s += x
end = time.time()

print(f"s:{len(s)}시간:{end-start}")


start = time.time()

s = "".join(map(str,strings))
end = time.time()
print(f"s:{len(s)}시간:{end-start}")


#string은 +보다는 foramt이나 join map쓰는 것이 좋음





lst = [1,2,3]
lst2 = lst
lst2[0] = 10



a = "hell"
b = a
b += "o"
print(a is b)



x="helloworld"
s= ""

for i in x:
    s += i
    print(f"{s},s의 메모리주소: {id(s)}")

