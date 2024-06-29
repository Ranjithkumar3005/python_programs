class rect:
    def __init__(self,len,wid):
        self.length=len
        self.width=wid
        
class area(rect):
    def __init__(self, len, wid):
        super().__init__(len, wid)
        print(len*wid)
        
area(10,20)