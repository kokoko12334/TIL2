
class Stack():
    def __init__(self):
        self.stack =[]
    
    def push(self, x):
        
        self.stack.append(x)

    def pop(self):
        pop_ = None
        if self.isempty():
            print("Stack is empty")
        else:
            pop_ = self.stack.pop()    
        return pop_

    def isempty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty   
    def top(self):

        if self.isempty():
            print('Stack is empty')
        else:
            print(self.stack[-1])


a = Stack()
a.push(2) #
a.isempty()
a.pop()
a.top()
