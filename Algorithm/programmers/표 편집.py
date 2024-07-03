from collections import deque
def solution(n, k, cmd):
    answer = ''
    def u_x(idx, x):
        return max(0, idx - x)
    def d_x(idx, x):
        return min(n-1, idx + x)
    def c(idx):
        nonlocal n
        v = lst[idx]
        lst.remove(v)
        del_rows.append((idx, v))
        # print(f"del추가:{(idx, v)}")
        n -= 1
        # print(f"변경된 길이:{n}")
        if idx == n:
            return idx - 1
        else:
            return idx
    def z(idx):
        add_idx, v = del_rows.pop()
        lst.insert(add_idx, v)
        if idx >= add_idx:
            return idx + 1
        else:
            return idx
        
    del_rows = []
    idx = k
    lst = deque([i for i in range(n)])
    nn = n
    for command in cmd:
        a = command[0]
        # print("##########")
        # print(f"실행 명령어:{a}, 현재 인덱스:{idx}, 현재 lst:{lst}, 삭제:{del_rows}")
        if a == 'D':
            x = int([i for i in command.split(" ")][1])
            idx = d_x(idx, x)
            # print(f"{x}만큼 이동 아래 :{idx}")
            
        elif a == "U":
            x = int([i for i in command.split(" ")][1])
            idx = u_x(idx, x)
            # print(f"{x}만큼 이동 위 :{idx}")
            
        elif a == "C":
            idx = c(idx)
            # print(f"삭제후 idx:{idx}")
            
        elif a == "Z":
            idx = z(idx)
            # print(f"복구 후 idx:{idx}")
            # print(f"복구후 lst:{lst}")
        
    
    # print(f"최종:{lst}")
    sett = set(lst)
    answer = []
    for i in range(nn):
        if i in sett:
            answer.append("O")
        else:
            answer.append("X")
    
    
    return "".join(answer)