class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        dum=[]
        arr=sorted(arr)
        n = len(arr)
        if n % 2 != 0:
            median = arr[n / 2]
        else:
            median = arr[(n-1) // 2]
        
        c=0
        while c!=k:
            if abs(arr[0] - median) > abs(arr[len(arr)-1] - median):
                dum.append(arr[0])
                arr.pop(0)
            else:
                dum.append(arr[len(arr)-1])
                arr.pop(len(arr)-1)  
            c+=1
        print(dum)

s=Solution()
s.getStrongest(arr = [6,7,11,7,6,8], k = 5)