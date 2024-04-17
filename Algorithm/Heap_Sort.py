import pickle
import time
from heapq import heapify, heappop, heappush
with open("./list_data.pickle", "rb") as f:
    lst = pickle.load(f)
n = len(lst)
# heapify => n , 모든 n에 대해서 heappop => logn => n+ nlogn

start = time.time()

sorted_lst = []
heapify(lst)
for _ in range(n):
    num = heappop(lst)
    sorted_lst.append(num)

end = time.time()
print("hepify 정렬걸린 시간: {}".format(end-start))

# #################################
# with open("./list_data.pickle", "rb") as f:
#     lst = pickle.load(f)
# n = len(lst)
# start = time.time()

# hq = []
# sorted_lst = []
# for i in lst:
#     heappush(hq, i)
# for _ in range(n):
#     num = heappop(lst)
#     sorted_lst.append(num)

# end = time.time()
# print("heappush 정렬걸린 시간: {}".format(end-start))
