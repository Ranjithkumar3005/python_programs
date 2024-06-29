class StockSpanner(object):

    def __init__(self):
        self.st=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.st==[] or self.st[len(self.st)-1][0]>price:
            self.st.append([price,1])
            return 1
        else:
            tem=0
            while self.st!=[] and self.st[len(self.st)-1][0]<=price:
                tem+=self.st[len(self.st)-1][1]
                self.st.pop()
            self.st.append([price,tem+1])
            return tem+1
# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(10)
param_2 = obj.next(80)
param_3 = obj.next(90)
param_4 = obj.next(170)
param_5 = obj.next(190)
param_6 = obj.next(275)
param_7 = obj.next(385)
print(param_7)