class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def recur(nums, check):
            # Base case: only one element remains
            if len(nums) == 1:
                return nums[0]
            
            dum = []
            if check:
                for i in range(1, len(nums), 2):
                    dum.append(nums[i])
            else:
                for i in range(len(nums)-2, -1,-2):
                    dum.append(nums[i])
                dum=dum[::-1]
            print(dum)
            return recur(dum, not check)
        
        nums = list(range(1, n + 1))
        return recur(nums, True)
        

s = Solution()
print(s.lastRemaining(6)) 
