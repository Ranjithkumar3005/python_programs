class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def permute(nums):
        
            res=[]
        
            if len(nums)==1:
                return [nums[:]]
        
            for i in range(len(nums)):
                n=nums.pop(0)
                perms=permute(nums)
                for perm in perms:
                    perm.append(n)
                res.extend(perms)
                nums.append(n)
            return res
        nums=[]
        for i in range(n):
            nums.append(i+1)
        val=permute(nums)
        val=sorted(val)
        val=val[k-1]
        val1=""
        for i in val:
            val1+=str(i)
        return val1
        
        
        

s=Solution()
print(s.getPermutation(n = 4, k = 9))