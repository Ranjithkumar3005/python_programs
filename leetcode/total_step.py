class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st=[nums[0]]
        i=1
        c=0
        while True:
            check=True
            lastele=st[-1]
            for i in range(1,len(nums)):
                if st[-1]>nums[i] and lastele>nums[i]:
                   lastele=nums[i]
                   check=False
                else:
                    st.append(nums[i])
                    lastele=nums[i]
            if check:
                break
            c+=1
            nums=st[:]
            st=[nums[0]]
        print(c)
                    
        
        

s=Solution()
s.totalSteps(nums = [4,5,7,7,13])