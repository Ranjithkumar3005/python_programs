class MapSum(object):

    def __init__(self):
        self.h={}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.h[key]=val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        self.sum=0
        for i in self.h:
            if i[:len(prefix)]==prefix:
                self.sum+=self.h[i]
        print(self.sum)
        


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("abcd",3)
obj.insert("abc",7)
param_2 = obj.sum("ab")

