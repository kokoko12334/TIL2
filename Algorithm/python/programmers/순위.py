


def dfs(idx, n,arr2):

    players = n -1
    visited = [0] * (n+1)
    visited[idx] = 1
    stack = [[idx,0]]
    cnt = 0
    while stack:
        idx,num = stack.pop()
        arr = arr2[idx]
        for i in range(1,n+1):

            if visited[i] == 0:

                if num == 0:
                    if arr[i] == 1:
                        stack.append([i,arr[i]])
                        visited[i] = 1
                        cnt += 1
                    elif arr[i] == -1:
                        stack.append([i,arr[i]])
                        visited[i] = 1
                        cnt += 1
                
                elif num == 1:
                    if arr[i] == 1:
                        stack.append([i,arr[i]])
                        visited[i] = 1
                        cnt += 1
                
                else:
                    if arr[i] == -1:
                       stack.append([i,arr[i]])
                       visited[i] = 1
                       cnt += 1   

    result = True
    if cnt != players:
        result = False

    return result



def solution(n, results):

    arr2 = [[0]*(n+1) for _ in range(n+1)]
    
    for i in results:
        win, lose = i

        arr2[win][lose] = -1
        arr2[lose][win] = 1


    answer = 0
    for idx in range(1,n+1):

        check = dfs(idx,n,arr2)

        if check:
            answer += 1

    return answer







print(solution(4, [[1,2],[1,3],[3,4]]))



