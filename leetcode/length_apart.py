class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        c = 0
        check = False
        
        for i in nums:
            if i == 1:
                if check and c < k:
                    return False
                check = True
                c = 0
            elif check:
                c += 1
        
        return True
    

s=Solution()
print(s.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))