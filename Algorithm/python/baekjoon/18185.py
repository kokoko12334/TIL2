
import sys

n = int(sys.stdin.readline())

lst = [int(i) for i in sys.stdin.readline().split()]

answer = 0
for i in range(n):
    if lst[i] == 0:
        continue
    while lst[i] > 0:
        di = {"one": 3, "two": 999999, "th": 9999999}
        if i+1 < n and lst[i+1]:
            di["two"] = 5/2
            num2 = min(lst[i], lst[i+1]) 

            if i+2 < n and lst[i+2]:
                if lst[i+1] > lst[i+2]:
                    num2 = lst[i+1]-lst[i+2]
                    pass
                else:
                    di["th"] = 7/3
                    num3 = min(lst[i], lst[i+1], lst[i+2])
                    
                    
        sor = sorted(di.items(), key = lambda x: x[1])
        ch = sor[0]
        if ch[0] == "one":
            answer += ch[1]
            lst[i] -= 1
        elif ch[0] == "two":
            answer += 5*num2
            lst[i] -= num2
            lst[i+1] -= num2
        else:
            answer += 7 *num3
            lst[i] -= num3
            lst[i+1] -= num3
            lst[i+2] -= num3


print(answer)
