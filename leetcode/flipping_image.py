class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        dum=[]
        
        for i in range(0,len(image)):
            val=reversed(image[i])
            dumm=[]
            for j in val:
                if j==1:
                    dumm.append(0)
                else:
                    dumm.append(1)
            dum.append(dumm)
        print(dum)
            
        
        

s=Solution()
s.flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])