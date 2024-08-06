class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x1=str(bin(x))[2:]
        x2=str(bin(y))[2:]
        c=0
        if len(x2)>=len(x1):
            x2=x2[::-1]
            for i in range(0,len(x2)):
                if len(x1)>i:
                    if x1[i]!=x2[i]:
                        c+=1
                else:
                    if x2[i]=="1":
                        c+=1
        
        else:
            x1=x1[::-1]
            for i in range(0,len(x1)):
                if len(x2)>i:
                    if x1[i]!=x2[i]:
                        c+=1
                else:
                    if x1[i]=="1":
                        c+=1
        print(c)
        

s=Solution()
s.hammingDistance( x = 1, y = 4)