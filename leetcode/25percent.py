class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length=len(arr)
        count=0
        dummy=arr[0]
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=0
                if (count==(len(arr)/4)) :
                    print(count)
                    dummy= (arr[i])
            else:
                count=1
        return dummy
    

    
s=Solution()
print(s.findSpecialInteger([1,1]))