


lst = [1,8,3,4,11,9,5,13,12,2,14]


###########dp방식################
n = len(lst)
dp = [1]*n
answer = {i: [lst[i]] for i in range(n)}
#dp[i] => 인덱스 (0<=j<= i-1)만큼 확인하여
#lst[i] >lst[j]이면 dp[i] = 기존의 값, dp[j] + 1해당값에서 +1을 비교한다.
for i in range(1,n):
    idx = 0
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[i] < dp[j] + 1:
                idx = j
            dp[i] = max(dp[i], dp[j]+1)
            
    
    answer[i] = answer[idx] + answer[i]    


for k,v in answer.items():
    print(k,v)


#############이분 탐색##############
#이분탐색의 아이디어는 16 보다는 13이 더 미래에 긴 수열을 가질것으로 기대된다는 것이다.
#이때 137 에서 그다음이 5라고 한다면 이분 탐색으로 5가 들어갈 자리를 찾는다
# 137 -> 135 그다음 2가 오면 2가 들어갈 자리를 찾는다.
# 135 -> 125 이때 135든 125든 개수에 차이는 없고 단순히 위의
#과정에서 일반적으로 처리하기 위해서 다음과 같이 되는 것이다.
#이때 만약 135에서 8이 왔다면 그대로 붙혀서 1358이다.
#이때 최종 배열 [1358]의 길이인 4가 길이가 된다.
#따라서 이분탐색은 LIS를 구할 수는 없고 길이만 알 수 있다.
#만약 배열도 알고 싶다면 끝에 들어온 것만(arr[-1]) 기록해주면 된다.

lst = [1,8,3,4,11,9,5,13,12,2,14]
n = len(lst)
lst2 = [lst[0]]

lst2[0] = lst[0]

for i in range(1,n):
    print(lst2)
    if lst[i] > lst2[-1]:
        lst2.append(lst[i])
    else:
        #여기서 이분 탐색(들어갈 자리 찾기)
        s = 0
        e = len(lst2)
        idxx = 0 
        while s <= e:
            idx = (s+e)//2
            if lst2[idx] < lst[i]:
                s = idx + 1
                idxx = s
            else:
                e = idx - 1
                idxx = s
        lst2[idxx] = lst[i]

print(len(lst2))


## 배열 알기
## 위 과정에서 lst2[-1]이 바뀌었으면 or 숫자가 크면 처리
lst = [1,8,3,4,11,9,5,13,12,2,14]
n = len(lst)
lst2 = [lst[0]]
lst2[0] = lst[0]
lis = [lst[0]]
for i in range(1,n):
    
    if lst[i] > lst2[-1]:
        lst2.append(lst[i])
        lis.append(lst[i])
    else:
        #여기서 이분 탐색(들어갈 자리 찾기)
        s = 0
        e = len(lst2) - 1
        
        while s <= e:
            idx = (s+e)//2
            if lst2[idx] < lst[i]:
                s = idx + 1
                
            else:
                e = idx - 1
                
        
        lst2[idx] = lst[i]
        
        if idx == len(lst2) - 1:
            lis[-1] = lst[i]

print(lis)


