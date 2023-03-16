import sys
sys.setrecursionlimit(1000) 
# l,c = [int(i) for i in sys.stdin.readline().split()]

# al = [i for i in sys.stdin.readline().split()]

# al = ['a','b','c','d']
# pwd = []




# def all_search(lst):
#     lst2 = []
#     for i in range(len(lst)):
#         lst2.append(lst[i])
#         for j in all_search(lst[i:]):
#             lst2.append(lst[j])
#     return lst2        

# all_search(al)


# 입력값(매개변수), 결과값(리턴값), 그리고 리턴 후 돌아갈 위치

def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)    


def fac2(n, total = 1):
    if n ==1:
        return total
    return fac2(n-1, n*total)    

# print(factorial(1001))
# print(fac2(1000))

#return address arguments local variables
def trisum(n, csum):
    while True:                     # Change recursion to a while loop
        if n == 0:
            return csum
        n, csum = n - 1, csum + n   # Update parameters instead of tail recursion

print(trisum(1000,0))
