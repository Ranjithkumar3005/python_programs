class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dummy=[]
        for i in range(0,len(nums)):
            str1=str(nums[i])
            dum=[]
            for i in str1:
                dum.append(int(i))
            max1=max(dum)
            str2=""
            for i in range(0,len(str1)):
                str2+=str(max1)
            dummy.append(int(str2))
        
        return sum(dummy)
            
        

s=Solution()
s.sumOfEncryptedInt(nums = [10,21,31])