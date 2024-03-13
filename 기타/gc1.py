import gc
print("")
print(gc.get_threshold())



gc.set_threshold(0)


class Some:
    def __init__(self,data=None):
        self.data = data
    def some(self):
        pass


gc.set_threshold(1000,100,10)
print(gc.get_threshold())


a = Some()
a.data = a

gc.get_objects(generation=1)

gc.get_count()
gc.collect(0)

gc.get_objects(generation=2)