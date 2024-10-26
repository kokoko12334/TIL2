def solution(expressions):
    arr = []
    no = []
    minn = 2
    for ex in expressions:
        if ex[-1] == "X":
            no.append(ex)
        else:
            arr.append(ex)
        a, op, b, _, c = ex.split()
        a_max = max([int(i) for i in a]) + 1
        b_max = max([int(i) for i in b]) + 1
        c_max = 0
        if c != "X":
            c_max = max([int(i) for i in c]) + 1
        minn = max(a_max, b_max, c_max, minn)
    def trans(n, num):
        summ = 0
        i = 0
        while num:
            summ += (num % 10) * (n**i)
            num = num // 10
            i += 1
        return summ
    def reverse(n, num):
        summ = []
        while num:
            summ.append(str(num % n))
            num = num // n
        summ.append("0")
        result = "".join(summ[::-1])
        return int(result)
        
    def cal(ex):
        nonlocal minn
        a, op, b, _, c = ex.split()
        a = int(a)
        b = int(b)
        c = int(c)
        sub2 = set(range(minn, 10))
        sub3 = set()
        for n in sub2:
            trans_a = trans(n, a)
            trans_b = trans(n, b)
            trans_c = trans(n, c)
            if op == "+":
                re = trans_a + trans_b
                if re == reverse(trans_c):
                    sub3.add(n)
            else:
                re = trans_a - trans_b
                if re == reverse(trans_c):
                    sub3.add(n)
        return sub3
    sub = set(range(2, 10))
    for ex in arr:
        result = cal(ex)
        sub = sub and result
        
    answer = []
    for ex in no:
        a, op, b, _, _ = ex.split()
        a = int(a)
        b = int(b)
        result = set()
        for n in sub:
            
            trans_a = trans(n, a)
            trans_b = trans(n, b)
            if op == "+":
                re = reverse(n, trans_a + trans_b)
            else:
                re = reverse(n, trans_a - trans_b)
            result.add(re)
        # print(f"{ex} -> {result}")
        if len(result) == 1:
            answer.append(ex[:-1] + str(list(result)[0]))
        else:
            answer.append(ex[:-1] + "?")
            
        
    return answer