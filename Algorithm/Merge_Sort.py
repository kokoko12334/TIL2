import pickle
import time
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)
n = len(lst)
start = time.time()

# 재귀에서 2개이하가 될때까지 쪼갠다.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 중간 지점을 찾아 배열을 나눕니다
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 각 반쪽을 재귀적으로 정렬합니다
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0  # 왼쪽 배열의 인덱스
        j = 0  # 오른쪽 배열의 인덱스
        k = 0  # 병합된 배열의 인덱스

        # 왼쪽과 오른쪽 배열의 요소들을 비교하며 병합합니다
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 왼쪽 배열에 남은 요소들을 병합합니다
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 오른쪽 배열에 남은 요소들을 병합합니다
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 예제 배열

merge_sort(lst)

end = time.time()
print("병합 정렬걸린 시간: {}".format(end-start))
