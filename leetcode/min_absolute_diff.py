class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr=sorted(arr)
        min1=10**6
        for i in range(0,len(arr)-1):
            val=arr[i+1]-arr[i]
            min1=min(min1,val)
        dum=[]
        for i in range(0,len(arr)-1):
            if arr[i+1]-arr[i]==min1:
                dum.append([arr[i],arr[i+1]])
        print(dum)

s=Solution()
s.minimumAbsDifference(arr = [4,2,1,3])