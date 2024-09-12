class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c={}
        for i in range(1,len(nums)-1):
            c1=i-1
            c2=i+1
            check=True
            if nums[i]==nums[c1]:
                while  c1!=0:
                    c1-=1
                    if nums[i]!=nums[c1]:
                        check=False
                        break
                if check:
                    continue
            
            if nums[i]==nums[c2]:
                while  c2!=len(nums)-1:
                    c2+=1
                    if nums[i]!=nums[c1]:
                        check=False
                        break
                if check:
                    continue
            
            if (nums[i]<nums[c1] and nums[i]<nums[c2]) or (nums[i]>nums[c1] and nums[i]>nums[c2]):
                c[nums[i]]=0
        print(len(c))

s=Solution()
s.countHillValley(nums = [6,6,5,5,4,1])