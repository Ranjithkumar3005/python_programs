class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a=[]
        b=[]
        c=[]
        for i in nums:
            if i<pivot:
                a.append(i)
            elif i>pivot:
                b.append(i)
            else:
                c.append(i)
        return a+c+b
        
        
        

s=Solution()
print(s.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))