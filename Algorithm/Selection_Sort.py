import pickle
import time
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)

# 인덱스 0부터 시작해서 가장 작은 값을 찾고 해당 최소값이라면 해당 인덱스 값과 바꾼다.
# arr[:], arr[1:], arr[2:] 순으로 가장 작은 값을 찾는다.
n = len(lst)

start = time.time()
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if lst[min_index] > lst[j]:
            min_index = j
            
    lst[i], lst[min_index] = lst[min_index], lst[i]

end = time.time()
print("선택 정렬걸린 시간: {}".format(end-start))

