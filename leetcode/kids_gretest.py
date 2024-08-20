class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        dum=[]
        max1=max(candies)
        for i in candies:
            if i+extraCandies>=max1:
                dum.append(True)
            else:
                dum.append(False)
        print(dum)
        
        

s=Solution()
s.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)