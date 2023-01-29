
#선형 큐
class Queue():
    def __init__(self):
        self.queue = []

    def isque(self):
        is_que = False
        if len(self.queue) ==0:
            is_que = True
            return is_que

    def enqueue(self, x):
        return self.queue.append(x)
    
    def dequeue(self):
        if self.isque():
            print('queue is empty')
        else:
            q_v = self.queue[0]
            del self.queue[0]
            return q_v

    def peek(self):
        if self.isque():
            print('queue is empty')
        else:
            return self.queue[0]    
        





#원형 큐

class C_queue():

    def __init__(self, len_):
        self.q = [None]*(len_+1)
        self.len_ = len_
        self.r = 0
        self.f = 0

    def isempty(self):
        is_empty = False
        if self.r == self.f:
            is_empty = True
            return is_empty
        return is_empty    

    def isfull(self):
        is_full = False
        if (self.r+1)%(self.len_+1) == self.f:
            is_full = True
            return is_full
        return is_full    

    def enqueue(self, x):

        if not self.isfull():
            self.r = (self.r+1)%(self.len_+1)
            self.q[self.r] = x
            return self.q
        else:
            print('초과입니다.')    

    def dequeue(self):
        
        if not self.isempty():
            self.f = (self.f+1)%(self.len_+1)
            self.q[self.f] = None
            return self.q
        else:
            print('비었습니다.')
    
    def print_queue(self):
 
        if not self.isempty() and self.r > self.f:
            return self.q[self.f+1:self.r+1]

        elif not self.isempty() and self.r < self.f:

            return self.q[:self.r+1]+self.q[self.f+1:]

        else:
            print('비었습니다.')




a = C_queue(4)

a.isfull()
a.isempty()

a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.dequeue()
a.print_queue()


# r>f인 경우
a.enqueue(5)
a.dequeue()
a.print_queue()













