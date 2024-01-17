for _ in range(int(input())):
    lst = []
    
    for _ in range(int(input())):  
        word = input()
        lst.append(word)
        pal = []
        
    for i in range(len(lst)):
        
        lst2 = lst.copy()
        start = lst2.pop(i)
        
        for j in range(len(lst2)):
            check = start+lst2[j]
            if check ==check[::-1]:
                pal.append(check)
                break
        if check == check[::-1]:
            break    
    if len(pal)==0:
        print(0)
    else:
        print(pal[0])    









