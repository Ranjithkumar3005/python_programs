class MyHashMap:
    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
key=1
value=2
obj = MyHashMap()
obj.put(key,value)
print(obj.data)
param_2 = obj.get(key)
print(param_2)
obj.remove(key)
print(obj)