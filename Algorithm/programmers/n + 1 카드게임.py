def solution(coin, cards):

    answer = 0
    n = len(cards)
    own = set()
    discard = set()
    ok = []
    
    for i in range(n//3):
        num = cards[i]
        num2 = n + 1 - num
        if num2 in own:
            ok.append((num,num2))
            own.remove(num2)
        else:
            own.add(num)
    
    round = 1
    idx = n//3
    while idx+1 < n:
        discard.add(cards[idx])
        discard.add(cards[idx+1])
        # print(f"round:{round}: ok:{ok},own:{own},discard:{discard}, coin:{coin}")
        if ok:
            round += 1
            ok.pop()
            idx += 2
        else:
            for num in discard:
                num2 = n + 1 - num
                    
                if num2 in own and coin >= 1:
                    ok.append((num,num2))
                    coin -= 1
                    own.remove(num2)
                    discard.remove(num)
                    break
            if not ok:
                lst = list(discard)
                for num in lst:
                    num2 = n + 1 - num
                    
                    if num2 in discard and coin >= 2:
                        ok.append((num,num2))
                        coin -= 2
                        discard.remove(num)
                        discard.remove(num2)
                        break       
            if ok:
                round += 1
                ok.pop()
                idx += 2
            else:
                break
    
    answer = round
    return answer