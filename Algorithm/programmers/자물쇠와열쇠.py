def rotate(key,n):
    new_key = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_key[i][n-j-1]= key[j][i]          
    return new_key

def check(key,lock,cnt,answer):
    n = len(key)
    m = len(lock)
    for i in range(m+n):
        for j in range(m+n):
            cnt2 = cnt
            for lock_y in range(i,-1,-1):
                for lock_x in range(j,-1,-1):
                    key_y = lock_y + (n-1-i)
                    key_x = lock_x + (n-1-j)
                    if 0 <= key_y < n and 0 <= key_x < n and 0 <= lock_x < m and 0 <= lock_y < m:
                        
                        if lock[lock_y][lock_x] == 0 and key[key_y][key_x] == 1:
                            cnt2 += 1
                        elif lock[lock_y][lock_x] == 0 and key[key_y][key_x] == 0:
                            pass
                        elif lock[lock_y][lock_x] == 1 and key[key_y][key_x] == 1:
                            cnt2 -= 1
                        elif lock[lock_y][lock_x] == 1 and key[key_y][key_x] == 0:
                            pass
                    
                    if cnt2 == answer:
                        
                        return True
    return False
    
def solution(key, lock):
    n = len(key)
    m = len(lock)
    answer = m*m
    cnt = 0
    for i in range(m):
        for j in range(m):
            if lock[i][j]:
                cnt += 1
    
    for _ in range(4):
        key2 = rotate(key,n)
        result = check(key2,lock,cnt,answer)
        if result:
            return True
        key = key2
            
    return False