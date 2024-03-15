import sys
import gc

class Some:
    def __init__(self,data=None):
        self.data = data
    def some(self):
        pass

a = Some()
b = Some()
a.data = b
b.data = a
c = Some(data=Some())

gc.get_objects(generation=0)


gc.collect()

del a
del b
gc.get_count()


gc.collect()

gc.get_objects(generation=1)

