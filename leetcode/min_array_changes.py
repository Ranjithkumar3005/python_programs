class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h={}
        for i in range(0,int(len(nums)/2)):
            tot=abs(nums[i]-nums[len(nums)-i-1])
            if tot in h:
                h[tot]+=1
            else:
                h[tot]=1
                
        target_diff = max(h, key=h.get)
        
        # Step 3: Calculate the minimum number of changes required
        changes = 0
        
        for i in range(0,int(len(nums)/2)):
            left = nums[i]
            right = nums[len(nums) - i - 1]
            diff = abs(left - right)
            
            if diff != target_diff:
                if (left + target_diff <= k or left - target_diff >= 0) or (right + target_diff <= k or right - target_diff >= 0):
                    changes += 1
                else:
                    changes += 2
        
        print(changes)
        
s=Solution()
s.minChanges( nums = [1,10,5,1,4,6,4,2,4,9,7,9,0,11], k = 12)