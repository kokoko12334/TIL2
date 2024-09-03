# 방향대로 결합을 해야한다.
import sys
from itertools import product
input = sys.stdin.readline

n = int(input())

m = []
for _ in range(n):
    m.append([int(i) for i in input().split()])

cases = list(product(["l","r","u","d"], repeat=5))

def move(direction, m):

    if direction == "l":
        for i in range(n):
            l = 0
            r = 0
            while True:
                while l < n-1 and m[i][l] == 0:
                    l += 1
                r = l + 1
                if r>= n:
                    break
                while r < n-1 and m[i][r] == 0:
                    r += 1
                if m[i][l] == m[i][r]:              
                    m[i][l] += m[i][r]
                    m[i][r] = 0
                l = r
                if l >= n:
                    break
            
            for i in range(n):
                for k in range(n-1):
                    for j in range(k, n-1):
                        j2 = j+1
                        if m[i][j] == 0 and m[i][j2] != 0:
                            m[i][j], m[i][j2] = m[i][j2], m[i][j]    

    elif direction == "r":
        for i in range(n):
            l = n-1
            r = n-1
            while True:
                while l >= 1 and m[i][l] == 0:
                    l -= 1
                r = l -1
                if r < 0:
                    break
                while r >= 1 and m[i][r] == 0:
                    r -= 1
                if m[i][l] == m[i][r]:              
                    m[i][l] += m[i][r]
                    m[i][r] = 0
                l = r
                if l < 0:
                    break
            
            for i in range(n):
                for k in range(n-1, 0, -1):
                    for j in range(k, 0, -1):
                        j2 = j-1
                        if m[i][j] == 0 and m[i][j2] != 0:
                            m[i][j], m[i][j2] = m[i][j2], m[i][j]

    elif direction == "u":
        for i in range(n):
            l = 0
            r = 0
            while True:
                while l < n-1 and m[l][i] == 0:
                    l += 1
                r = l + 1
                if r>= n:
                    break
                while r < n-1 and m[r][i] == 0:
                    r += 1
                if m[l][i] == m[r][i]:              
                    m[l][i] += m[r][i]
                    m[r][i] = 0
                l = r
                if l >= n:
                    break
            
            for i in range(n):
                for k in range(n-1):
                    for j in range(k, n-1):
                        j2 = j+1
                        if m[j][i] == 0 and m[j2][i] != 0:
                            m[j][i], m[j2][i] = m[j2][i], m[j][i] 

    elif direction == "d":
        for i in range(n):
            l = n-1
            r = n-1
            while True:
                while l >= 1 and m[l][i] == 0:
                    l -= 1
                r = l -1
                if r < 0:
                    break
                while r >= 1 and m[r][i] == 0:
                    r -= 1
                if m[l][i] == m[r][i]:              
                    m[l][i] += m[r][i]
                    m[r][i] = 0
                l = r
                if l < 0:
                    break
            
            for i in range(n):
                for k in range(n-1, 0, -1):
                    for j in range(k, 0, -1):
                        j2 = j-1
                        if m[j][i] == 0 and m[j2][i] != 0:
                            m[j][i], m[j2][i] = m[j2][i], m[j][i]
    
    return m

answer = 0
for case in cases:
    m2 = [i[:] for i in m]
    for c in case:
        m2 = move(c, m2)

    for i in range(n):
        for j in range(n):
            answer = max(answer, m2[i][j])

print(answer)
