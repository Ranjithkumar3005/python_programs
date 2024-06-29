class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr=sorted(arr,reverse=True)
        print(arr)
        c=0
        
        k1=0
        dummy=[]
        for i in range(0,len(arr)):
            dum=arr[c]
            dummy.append(dum)
            k1+=1
            if k1==k:
                c+=1
                k1=0
        sum=0
        for i in dummy:
            sum+=i
        print(sum)
            
        
        
s=Solution()
s.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4)