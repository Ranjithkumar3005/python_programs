class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        que=[]
        check=False
        tot=0
        for i in range(0,len(nums)):
            que.append(nums[i])
            if (nums[i]==0 and check==False)or(que!=[] and que[0]==0):
                check=True
            if check:
                c+=1
            if c==k:
                tot+=1
                c=0
                check=False
                print(que)
                for i in range(0,k):
                    if que[i]==0:
                        que[i]=1
                    else:
                        c+=1
                        que[i]=0
                print(que)
                
            if que[0]==1:
                que.remove(1)
        if tot==0:
            return -1
        return tot
        
s=Solution()
s.minKBitFlips(nums = [1,1,0], k = 2)