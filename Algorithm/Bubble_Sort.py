import pickle
import time
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)
n = len(lst)
start = time.time()

for i in range(n):
    for j in range(n-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

end = time.time()
print("버블 정렬걸린 시간: {}".format(end-start))
