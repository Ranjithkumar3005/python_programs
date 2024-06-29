import random
class RandomizedCollection(object):

    def __init__(self):
        self.h={}
        self.d=[]
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        self.d.append(val)
        if val not in self.h:
            self.h[val]=1
            return True
        else:
            self.h[val]+=1
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.h:
            self.d.remove(val)
            self.h[val]-=1
            if self.h[val]==0:
               self.h.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.h)==0:
            return "null"
        return random.choice(self.d)


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()

