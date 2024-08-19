class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        c=0
        for i in range(0,len(arr1)):
            check=True
            for j in range(0,len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    check=False
                    break
            if check:
                c+=1
        print(c)
        
        

s=Solution()
s.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2)