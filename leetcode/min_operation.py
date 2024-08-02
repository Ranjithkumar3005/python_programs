import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        que=[]
        for i in range(0,len(nums)):
            heapq.heappush(que, nums[i])
        c=0
        while True:
            if len(que)<=1:
                break
            val1= heapq.heappop(que)
            val2= heapq.heappop(que)
            sum=(min(val1,val2)*2)+max(val1,val2)
            heapq.heappush(que,sum)
            if val1>=k:
                break
            c+=1
        print(c)
        
        

s=Solution()
s.minOperations(nums = [1,1,2,4,9], k = 20)