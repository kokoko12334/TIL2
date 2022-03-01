while True:
    
    a,b = map(int, input().split())
    if a==0 and b == 0:    
        break
    print(a+b)



#True로 무한루프, break 걸면 아무것도 안나오고 탈출함.
#이때 순서가 if가 중간에 끼는데 만약 if를 맨마지막에 둔다면
#print(a+b) = 0+0이 출력되고 그다음 break되어서 다음과 같이 해야함.


