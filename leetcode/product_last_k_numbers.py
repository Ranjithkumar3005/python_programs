class ProductOfNumbers(object):

    def __init__(self):
        self.A = [1]

    def add(self, a):
        if a == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * a)

    def getProduct(self, k):
        if k >= len(self.A): return 0
        return self.A[-1] / self.A[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(8)
obj.add(4)
obj.add(0)
obj.add(2)
obj.add(7)
param_2 = obj.getProduct(3)
print(param_2)