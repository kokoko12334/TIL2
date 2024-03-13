import sys

class Some:
    def some(self):
        pass

# a = Some()
# print(f"클래스Some의 참조 수: {sys.getrefcount(Some)}개")
# print(f"변수a의 참조 수: {sys.getrefcount(a)}개")



import gc
referrers = gc.get_referrers(Some)
for i in range(len(referrers)):
    print(f"클래스 생성시 기본참조{i}: {referrers[i]}")





class Some:
    def __init__(self,data=None):
        self.data = data
    def some(self):
        pass
 

a = Some()
b = a

# del b
# print(b)
# print(id(a))
# print(id(b))

gc.set_debug(1)