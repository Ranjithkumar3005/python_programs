from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self)==self.capacity and key not in self:
            self.popitem(last=False)
        
        self[key]=value
        self.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get(1)
obj.put(1,2)