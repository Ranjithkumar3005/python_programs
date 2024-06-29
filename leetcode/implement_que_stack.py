class MyQueue:

    def __init__(self):
        self.st=[]
        

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        dum=self.st[0]
        self.st.remove(dum)
        return dum

    def peek(self) -> int:
        return self.st[0]
        

    def empty(self) -> bool:
        if self.st==[]:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_4)
