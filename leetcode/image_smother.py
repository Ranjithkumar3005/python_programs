import math


class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        dummy=img[0]
        dummy1=img[1]
        dummy2=img[2]
        var1=math.floor((dummy[0]+dummy[1]+dummy1[0]+dummy1[1])/4)
        var2=math.floor((dummy[0]+dummy[1]+dummy1[0]+dummy1[1]+dummy[2]+dummy1[2])/6)
        var3=math.floor((dummy[1]+dummy[2]+dummy1[1]+dummy1[2])/4)
        var4=math.floor((dummy[0]+dummy[1]+dummy1[0]+dummy1[1]+dummy2[0]+dummy2[1])/6)
        var5=math.floor((dummy[0]+dummy[1]+dummy[2]+dummy1[0]+dummy1[1]+dummy1[2]+dummy2[0]+dummy2[1]+dummy2[2])/9)
        var6=math.floor((dummy[2]+dummy[1]+dummy1[2]+dummy1[1]+dummy2[2]+dummy2[1])/6)
        var7=math.floor((dummy2[0]+dummy2[1]+dummy1[0]+dummy1[1])/4)
        var8=math.floor((dummy2[0]+dummy2[1]+dummy1[0]+dummy1[1]+dummy[2]+dummy1[2])/6)
        var9=math.floor((dummy2[1]+dummy2[2]+dummy1[1]+dummy1[2])/4)
        dummy=[]
        dummy.append(var1)
        dummy.append(var2)
        dummy.append(var3)
        dummy1=[]
        dummy1.append(var4)
        dummy1.append(var5)
        dummy1.append(var6)
        dummy2=[]
        dummy2.append(var7)
        dummy2.append(var8)
        dummy2.append(var9)
        
        imag=[]
        imag.append(dummy)
        imag.append(dummy1)
        imag.append(dummy2)
        print(imag)
s=Solution()
s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]])