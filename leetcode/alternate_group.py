class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        c=0
        
        for i in range(1,len(colors)-1):
            if colors[i]!=colors[i-1] and colors[i]!=colors[i+1]:
                c+=1
        if colors[0]!=colors[1] and colors[0]!=colors[len(colors)-1]:
                c+=1
        if colors[len(colors)-1]!=colors[len(colors)-2] and colors[len(colors)-1]!=colors[0]:
                c+=1       
        print(c)
        

s=Solution()
s.numberOfAlternatingGroups( colors = [0,1,0,0,1])