from fractions import Fraction
import sys
input = sys.stdin.readline
n = int(input())

pattern = "".join([i for i in input().split()])
text = "".join([i for i in input().split()])
text += text[:-1]

def kmp_search(text, pattern):
    pi = compute_pi(pattern)
    j = 0  
    n_text = len(text)
    n_pattern = len(pattern)
    found_indexes = []

    for i in range(n_text):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            if j == n_pattern - 1:
                found_indexes.append(i - j)
                j = pi[j]
            else:
                j += 1

    return found_indexes

def compute_pi(pattern):
    n = len(pattern)
    pi = [0] * n 
    j = 0 
    
    for i in range(1, n):

        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1] 

        if pattern[i] == pattern[j]:
            j += 1 
            pi[i] = j 

    return pi

result = kmp_search(text, pattern)
son = len(result)
if son < n:
    fraction = Fraction(son, n)
    print(fraction)
else:
    print("1/1")