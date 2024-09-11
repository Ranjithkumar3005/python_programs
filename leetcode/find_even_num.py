class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        vals=set()
        
        
        for i in range(0,len(digits)):
            for j in range(0,len(digits)):
                for k in range(0,len(digits)):
                    if j!=k:
                        dum=str(digits[i])+str(digits[j])+str(digits[k])
                        if int(dum)%2==0:
                            vals.add(int(dum))
                    
        print(vals)
        

s=Solution()
s.findEvenNumbers(digits = [2,2,8,8,2])