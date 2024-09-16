class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = list(range(1, n+1))
        
        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(start, n):
                curr.append(nums[i])
                dfs(i + 1, curr) 
                curr.pop()  
        
        dfs(0, [])
        return res

s = Solution()
print(s.combine(n=4, k=2))
