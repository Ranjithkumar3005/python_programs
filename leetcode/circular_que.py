class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k=k
        self.st=[]
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.st)!=self.k:
            self.st.append(value)
            return True
        return False
        
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.st!=[]:
            m=self.st[0]
            self.st.remove(m)
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        if self.st==[]:
            return -1
        return self.st[0]

    def Rear(self):
        """
        :rtype: int
        """
        if self.st==[]:
            return -1
        return self.st[len(self.st)-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.st==[]:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.st)==self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_11 = obj.enQueue(2)
param_13 = obj.enQueue(21)
param_12 = obj.enQueue(21)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
print(param_6)