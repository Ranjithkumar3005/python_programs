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
            c+=1
            if check:
                break
            nums=st[:]
            st=[]
        print(c)
                    
        
        

s=Solution()
s.totalSteps(nums = [5,3,4,4,7,3,6,11,8,5,11])