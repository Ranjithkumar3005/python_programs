class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        while len(nums)!=1:
            arr=[]
            check=True
            for i in range(0,len(nums),2):
                if check:
                    arr.append(min(nums[i],nums[i+1]))
                    check=False
                else:
                    arr.append(max(nums[i],nums[i+1]))
                    check=True
            nums=arr[:]
            arr=[]
        print(nums[0])
s=Solution()
s.minMaxGame(nums = [1,3,5,2,4,8,2,2])