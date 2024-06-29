class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.sum=0
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        for i in range(left,right+1):
            self.sum+=self.nums[i]
        return self.sum
        
        


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(2,5)
print(param_1)