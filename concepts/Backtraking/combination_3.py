class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = list(range(1, n+1))
        
        def dfs(start, curr,tot):
            if len(curr) == k and tot==n:
                res.append(curr[:])
                return
            if tot>n or len(curr)>k:
                return
            
            for i in range(start, 9):
                curr.append(nums[i])
                dfs(i + 1, curr,tot+nums[i]) 
                curr.pop()  
        
        dfs(0, [],0)
        return (res)

s=Solution()
print(s.combinationSum3(k = 3, n = 9))