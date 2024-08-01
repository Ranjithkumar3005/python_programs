class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        dum=[]
        
        for i in range(0,len(queries)):
            check=True
            for i in range(queries[i][0],queries[i][1]):
              if ((nums[i]%2==0) and nums[i+1]%2!=0) or ((nums[i]%2!=0) and nums[i+1]%2==0):
                 continue
              else:
                 dum.append(False)
                 check=False
                 break
            if check:
              dum.append(True)
        
        print(dum)

s=Solution()
print(s.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))