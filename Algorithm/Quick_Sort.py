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


def quicksort(arr, low, high):
    if low < high:
        # 파티션 함수를 통해 피벗의 위치를 정하고, 피벗을 기준으로 배열을 나눈다
        pi = partition(arr, low, high)

        # 피벗 왼쪽 부분을 재귀적으로 정렬
        quicksort(arr, low, pi - 1)
        # 피벗 오른쪽 부분을 재귀적으로 정렬
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # 피벗을 배열의 마지막 요소로 선택
    pivot = arr[high]
    i = low - 1  # i는 피벗보다 작은 요소의 인덱스 i는 피봇보다 작은 인덱스임 -1은 현재 없다는 뜻

    for j in range(low, high):
        # 현재 요소가 피벗보다 작거나 같으면 i를 증가시키고 arr[i]와 arr[j]를 교환
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗을 올바른 위치로 이동
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

quicksort(lst, 0, n - 1)

end = time.time()
print("퀵 정렬걸린 시간: {}".format(end-start))
