

lst = [1,2,3]
###반복 과정 눈으로 확인
result = []
for i in range(len(lst)): 
    lst2 = lst[:i]+lst[i+1:]
    a = lst[i]
    for j in range(len(lst2)):
        lst3 = lst2[:j]+lst2[j+1:]
        b = lst2[j]
        for k in range(len(lst3)):
            c = lst3[k]
            result2 = [a,b,c]
            
            result.append(result2)
print(result)
lst = [1,2,3,4,5]
#위 과정을 재귀함수로 표현
def per(lst, n):
    result = []
    if n== 0:
        return [[]]

    for i in range(len(lst)):
        a = lst[i]
        
        lst2 = lst[:i] + lst[i+1:]            
        for j in per(lst2, n-1):
            print(j)
            result.append([a]+j)
    return result    
    
per(lst,5)



def f(n):
    if n == 0 or n ==1:
        return 1
    return n*f(n-1)


f(5)

k = 5
result = [0]*3
n = 3
lst = [1,2,3]

for i in range(n):
    
    fac = f(n-(i+1))
    
    if k%fac == 0:
        ad =  k/fac
        prior_num = ad-1
        k -= prior_num*fac
    
    elif k%fac != 0:
        ad2 = (k//fac) 
        ad = ad2 + 1
        prior_num = ad2
        k -= prior_num*fac
    ad  = int(ad)
    result[i] = lst[ad-1]
    next_ = ad-1
    lst = lst[:next_]+lst[next_+1:]


result
