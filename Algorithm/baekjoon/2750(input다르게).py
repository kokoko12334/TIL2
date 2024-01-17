###내가 쓰던거
a = []
for _ in range(int(input())):
    a.append(int(input()))
print(a)


#컴프리헨션을 이용함.
t = int(input())
lst = [int(input()) for _ in range(t)]


print(*sorted(lst), sep='\n')   #언팩킹 for문없이 가능




