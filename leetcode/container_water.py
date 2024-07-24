class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        ans=0
        
        while left<right:
            ans=max(ans,min(height[left],height[right])*(right-left))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        print(ans)
        
        

s=Solution()
s.maxArea(height = [1,8,6,2,5,4,8,3,7])