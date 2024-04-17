import pickle
import time
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)
n = len(lst)
start = time.time()

# 첫번째 원소는 정렬되었다고 가정하고 그 다음 숫자부터 삽입할 위치를 찾는다. 반복해서 (기본은)
# 앞에 있는 거는 정렬이 되어 있다고 가정한다. => 그래서 만약 정렬이 어느정도 되어있으면 n*n이라도 속도 가 버블, 선택정렬보다 빠르다.
for i in range(1, n):
    tmp = lst[i]
    idx = i - 1
    while idx >= 0 and tmp < lst[idx]:
        lst[idx+1] = lst[idx]
        idx = idx - 1
        i -= 1
    lst[idx+1] = tmp

end = time.time()
print("삽입 정렬걸린 시간: {}".format(end-start))
