from collections import deque
class LRUCache:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.current_size = 0
        self.q = deque()
        self.hash = dict()
        
    def get(self, key: int) -> int:
        
        if key not in self.hash:
            return -1
        
        self.q.remove(key)
        self.q.append(key)
        return self.hash[key]

    def put(self, key: int, value: int) -> None:
        
        if key in self.hash:
            self.q.remove(key)
            self.q.append(key)
            self.hash[key] = value
            return

        if self.current_size < self.size:
            self.q.append(key)
            self.hash[key] = value
        else:
            remove_key = self.q.popleft()
            self.hash.pop(remove_key)

            self.q.append(key)
            self.hash[key] = value

        self.current_size += 1











# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)