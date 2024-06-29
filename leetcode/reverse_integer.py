class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        dummy=str(x)
        dummy1=""
        if dummy[0]=="-" or dummy[0]=="+":
            dummy1+=dummy[len(dummy)-1:0:-1]
            dummy1=dummy[0]+dummy1
        else:
            dummy1+=dummy[len(dummy)-1:0:-1]
            dummy1+=dummy[0]
        dummy1=int(dummy1)
        if dummy1<-2**31 or dummy1>2**31:
            return 0
        return dummy1
        
s=Solution()
print(s.reverse(123))