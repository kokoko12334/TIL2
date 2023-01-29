import pickle
import time
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)


start = time.time()

for i in range(len(lst)-1):
    min_index = i
    for j in range(i+1, len(lst)):
        if lst[min_index] > lst[j]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

end = time.time()


print("선택 정렬걸린 시간: {}".format(end-start))
