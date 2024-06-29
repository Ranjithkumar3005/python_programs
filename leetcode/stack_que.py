class MyStack(object):

    def __init__(self):
        self.st=[]
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        dum= self.st[len(self.st)-1]
        self.st.pop()
        return dum

    def top(self):
        """
        :rtype: int
        """
        return self.st[len(self.st)-1]

    def empty(self):
        """
        :rtype: bool
        """
        print(self.st)
        if len(self.st)==0 : return True
        else:return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
#obj.push(2)
param_2 = obj.pop()
#param_3 = obj.top()
param_4 = obj.empty()
print(param_2," ",param_4)