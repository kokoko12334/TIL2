a,b,v = [int(i) for i in input().split()]

if (v-a)%(a-b) != 0:
    print(int((v-a)/(a-b))+2)
else:
    print(int((v-a)/(a-b))+1)

 