class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        dum=[]
        
        for i in range(0,len(nums)):
            sum1=nums[i]
            sum=nums[i]
            dum.append(sum)
            check=True
            for j in range(i+1,len(nums)):
                if check:
                  dum.append(sum+nums[j])
                  sum1+=nums[j]
                  check=False
                else:
                  sum1+=nums[j]
                  dum.append(sum1)
        dum=sorted(dum)
        sum=0
        for i in range(left-1,right):
          sum+=dum[i]
        
        print(sum)

s=Solution()
s.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10)