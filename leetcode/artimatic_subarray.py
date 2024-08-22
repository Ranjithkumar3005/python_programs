class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        dum=[]
        
        for i in range(0,len(l)):
            arr=nums[l[i]:r[i]+1]
            arr=sorted(arr)
            if len(arr)<=2:
                dum.append(True)
            else:
                sum=arr[0]-arr[1]
                check=True
                for j in range(1,len(arr)-1):
                    if sum!=arr[j]-arr[j+1]:
                        check=False
                        break
                dum.append(check)
        print(dum)

s=Solution()
s.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])