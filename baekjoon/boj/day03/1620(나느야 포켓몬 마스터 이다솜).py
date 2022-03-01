#https://www.acmicpc.net/problem/1620
n, m  = map(int, input().split())

key  = range(1,n+1)

value = [input() for _ in range(n)] 

pokemon = dict(zip(key, value))

test =[input() for _ in range(m)]
for i in range(len(test)):
    try: 
        test[i] = int(test[i])
    except:
        pass

#숫자면 키값으로 스트링이면 밸류로 찾아야함.
for i in test:
    if type(i) is int:
        print(pokemon[i])
    elif type(i) is str:
        r = [k for k, v in pokemon.items() if v==i]
        print(r[0])









# ##########정답
# n, m = map(int, input().split())

# numbers = {}
# names = {}

# for i in range(1, n+1):
# 	name = input()
# 	numbers[name] = i
# 	names[i] = name

# for _ in range(m):
# 	value = input()
# 	if value.isdecimal():
# 		print(names[int(value)])
# 	else:
# 		print(numbers[value])
