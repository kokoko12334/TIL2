import pickle
import time
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)
n = len(lst)
start = time.time()
# 피봇을 기준으로 왼쪽 포인터는 피봇보다 작은수 오른쪽 포인터는 피봇보다 큰 수를 만족해야 한다. => 퀵 셀렉트
# 퀵셀렉트는 만약 전체 10개에서 2번째 큰수를 찾고자 할때 인덱스는 8이다.(9,8) => 이때 퀵셀렉트로 피봇을 잡고 해당 피봇이 4번째에 위치한다면
# 피봇의 오른쪽에 8번째인덱스(2번째로 큰수)가 있으므로 탐색범위는 반으로 줄어드는 식이다. 
# 퀵 소트는 퀵셀렉트를 재귀적으로 수행


def partition(lst,l,r):
    pivot = lst[-1]
    
    while l < r:
        if lst[l] < pivot:
            l += 1
        if lst[r] > pivot:
            r -= 1





end = time.time()
print("퀵 정렬걸린 시간: {}".format(end-start))
