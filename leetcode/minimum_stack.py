from collections import defaultdict


class FreqStack(object):

    def __init__(self):
        self.stks = []
        self.freq = defaultdict(int)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        if self.freq[val] > len(self.stks):
            self.stks.append([val])
        else:
            self.stks[self.freq[val]-1].append(val)
    
    def pop(self):
        """
        :rtype: int
        """
        val = self.stks[-1].pop()
        if not self.stks[-1]:
            self.stks.pop()
        self.freq[val] -= 1
        return val
                

# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.pop()
param_5 = obj.pop()
print(param_5)