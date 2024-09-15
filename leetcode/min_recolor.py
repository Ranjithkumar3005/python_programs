class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min1=999999999
        for i in range(0,len(blocks)-k):
            c=0
            for j in range(i,i+k):
                if blocks[j]!="B":
                    c+=1
            min1=min(c,min1)
        print(min1)


s=Solution()
s.minimumRecolors(blocks = "WBBWWBBWBW", k = 7)