class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        
        h={}
        c=1
        for i in range(0,len(nums)):
            if nums[i]==x:
                h[c]=i
                c+=1
        dum=[]
        for i in range(0,len(queries)):
            if queries[i] in h:
                dum.append(h[queries[i]])
            else:
                dum.append(-1)
        print(dum)
        

s=Solution()
s.occurrencesOfElement( nums = [1,3,1,7], queries = [1,3,2,4], x = 1)