class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        c1=ord(coordinates[0])
        c2=int(coordinates[1])
        if (c1%2==0 and c2%2==0) or (c1%2!=0 and c2%2!=0):
            return False
        return True
        
        
        
s=Solution()
print(s.squareIsWhite(coordinates = "h6"))